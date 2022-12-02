class status:
    NO_DATA = 6


STATUS = { 
    'SUCCESS': 1,
    'NOT_LOGIN': 2,
    'NOT_PERMISSION': 3,
    'INPUT_INVALID': 4,
    'TOKEN_EXPIRED': 5,
    'NO_DATA': 6,
    'FAIL_REQUEST': 7
}

ERROR = {
    'NOT_EXISTS_POST': 'Post is not exists.',
    'EXISTS_SAVE_POST': 'This post is saved.',
    'EXISTS_POST_REACT': 'React is existed.',
    'NOT_EXISTS_SAVE_POST': 'This post is not saved.',
    'NOT_EXISTS_POST_REACT': 'This post is not reacted.',
    'EDIT_FAIL':'Edit fails.',
    'POST_NO_TRASH':'Post has not in trash.',
    'NOT_EXISTS_USER_ID':'User_id is not found.',
    'NOT_EXISTS_POST_ID':'Post_id is not found.',
    'NOT_EXISTS_REACT':'React is not found.',
    'MESSAGE_INPUT':'Message has not been intered.',
    'NOT_EXISTS_COMMENT':'Comment is not exists.',
    'NOT_EXISTS_GROUP':'Group is not exists.',
}

SUCCESS = {
    'POST_BLOG': 'Post is posted.',
    'EDIT_POST': 'Post is edited.',
    'DELETED_POST': 'Post is deleted.',
    'DROP_POST': 'Post is droped.',
    'RESTORE_POST': 'Restore is success.',
    'SAVE_POST': 'Post is saved.',
    'UNSAVE_POST': 'Post is unsaved.',
    'REACT_POST': 'React is saved.',
    'UN_REACT_POST': 'React is unsaved.',
    'COMMENT_POST': 'Comment is success.',
    'DROP_COMMENT': 'Comment is success.',
    'ADD_GROUP': 'Group was added success.',
    'DELETE_GROUP': 'Group was added success.',
}