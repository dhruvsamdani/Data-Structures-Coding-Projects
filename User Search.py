class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    def group_in_group(group):
        if group.get_groups() == []:
            return group
        for group in group.get_groups():
            group = group_in_group(group)
        return group

    for user1 in group_in_group(group).get_users():

        if user1 == user:
            return True

    return False

print(is_user_in_group('sub_child_user',sub_child)) # True
print(is_user_in_group(None,sub_child)) # False
print(is_user_in_group(4432982983,parent)) # False