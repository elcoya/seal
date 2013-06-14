def user_is_undergraduate(user):
    return len(user.student_set.all()) > 0
