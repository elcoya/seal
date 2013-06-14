def user_is_teacher(user):
    return len(user.teacher_set.all()) > 0
