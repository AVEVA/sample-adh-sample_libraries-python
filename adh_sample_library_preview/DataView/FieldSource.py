from enum import Enum


class FieldSource(Enum):
    """
    enum 0-12 fully inclusive
    """
    NotApplicable = 0
    Id = 1
    Name = 2
    PropertyId = 3
    PropertyName = 4
    Metadata = 5
    Tags = 6
    TenantId = 7
    TenantName = 8
    NamespaceId = 9
    NamespaceName = 10
    CommunityId = 11
    CommunityName = 12
