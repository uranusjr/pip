import email.parser
import logging

from pip._vendor import pkg_resources
from pip._vendor.packaging.utils import canonicalize_name
from pip._vendor.packaging.version import _BaseVersion

from pip._internal.exceptions import NoneMetadataError
from pip._internal.utils import misc  # TODO: Move definition here.
from pip._internal.utils.packaging import get_installer
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

from .base import BaseDistribution, BaseEnvironment

if MYPY_CHECK_RUNNING:
    from typing import Iterator, List, Mapping, Optional


logger = logging.getLogger(__name__)


class Distribution(BaseDistribution):
    def __init__(self, dist):
        # type: (pkg_resources.Distribution) -> None
        self._dist = dist

    @property
    def canonical_name(self):
        # type: () -> str
        return canonicalize_name(self._dist.project_name)

    @property
    def version(self):
        # type: () -> _BaseVersion
        return self._dist.parsed_version

    @property
    def installer(self):
        # type: () -> str
        return get_installer(self._dist)

    @property
    def editable(self):
        # type: () -> bool
        return misc.dist_is_editable(self._dist)

    @property
    def local(self):
        # type: () -> bool
        return misc.dist_is_local(self._dist)

    @property
    def in_usersite(self):
        # type: () -> bool
        return misc.dist_in_usersite(self._dist)

    @property
    def metadata(self):
        # type: () -> Mapping[str, str]
        metadata_name = "METADATA"
        if (isinstance(self._dist, pkg_resources.DistInfoDistribution) and
                self._dist.has_metadata(metadata_name)):
            metadata = self._dist.get_metadata(metadata_name)
        elif self._dist.has_metadata("PKG-INFO"):
            metadata_name = "PKG-INFO"
            metadata = self._dist.get_metadata(metadata_name)
        else:
            logger.warning(
                "No metadata found in %s",
                misc.display_path(self._dist.location),
            )
            metadata = ""
        if metadata is None:
            raise NoneMetadataError(self, metadata_name)
        feed_parser = email.parser.FeedParser()
        feed_parser.feed(metadata)
        return feed_parser.close()


class Environment(BaseEnvironment):
    def __init__(self, ws):
        # type: (pkg_resources.WorkingSet) -> None
        self._ws = ws

    @classmethod
    def default(cls):
        # type: () -> BaseEnvironment
        return cls(pkg_resources.working_set)

    @classmethod
    def from_paths(cls, paths):
        # type: (Optional[List[str]]) -> BaseEnvironment
        return cls(pkg_resources.WorkingSet(paths))

    def _search_distribution(self, name):
        # type: (str) -> Optional[BaseDistribution]
        """Find a distribution matching the ``name`` in the environment.

        This searches from *all* distributions available in the environment, to
        match the behavior of ``pkg_resources.get_distribution()``.
        """
        canonical_name = canonicalize_name(name)
        for dist in self.iter_distributions():
            if dist.canonical_name == canonical_name:
                return dist
        return None

    def get_distribution(self, name):
        # type: (str) -> Optional[BaseDistribution]

        # Search the distribution by looking through the working set.
        dist = self._search_distribution(name)
        if dist:
            return dist

        # If distribution could not be found, call working_set.require to
        # update the working set, and try to find the distribution again.
        # This might happen for e.g. when you install a package twice, once
        # using setup.py develop and again using setup.py install. Now when
        # running pip uninstall twice, the package gets removed from the
        # working set in the first uninstall, so we have to populate the
        # working set again so that pip knows about it and the packages gets
        # picked up and is successfully uninstalled the second time too.
        try:
            # We didn't pass in any version specifiers, so this can never
            # raise pkg_resources.VersionConflict.
            self._ws.require(name)
        except pkg_resources.DistributionNotFound:
            return None
        return self._search_distribution(name)

    def iter_distributions(self):
        # type: () -> Iterator[BaseDistribution]
        for dist in self._ws:
            yield Distribution(dist)
