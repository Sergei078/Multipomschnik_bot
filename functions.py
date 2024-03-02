from SQL3 import (Add_promt, promt_user, requests_user, Add_requests, Add_subject,
                  subject_user, Add_level, level_user, Add_Question, question_user)
import logging
from ERROR import error5
from text import Profile, answer
from System_setting_gpt import  system


def info_db(user_id, name):
    try:
        requests = requests_user()
        subject = subject_user()
        level = level_user()
        try:
            req = requests.promt1(user_id)
            sub = subject.subject(user_id)
            lev = level.level(user_id)
        finally:
            requests.close()
            level.close()
            subject.close()
        info = Profile(name, sub, lev, req)
        return info
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def promt_db(promt, user_id):
    try:
        Question = Add_Question()
        subject = subject_user()
        level = level_user()
        try:
            Question.add_Question(promt, user_id)
            sub = subject.subject(user_id)
            lev = level.level(user_id)
        finally:
            Question.close()
            level.close()
            subject.close()
        system_content = system(sub, lev)
        return system_content
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def promt_add(n1, user_id, result):
    try:
        add_promt = Add_promt()
        question = question_user()
        try:
            question1 = question.Question(user_id)
            add_promt.add_pomt(n1, user_id)
        finally:
            question.close()
            add_promt.close()
        an = answer(question1, result)
        return an
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def Quantity(user_id):
    try:
        requests = requests_user()

        try:
            req = requests.promt1(user_id)
            adding = req + 1
        finally:
            requests.close()
        add_requests = Add_requests()
        try:
            add_requests.add_requests(adding, user_id)
        finally:
            add_requests.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def Continue(user_id):
    try:
        pr = promt_user()
        try:
            promt1 = pr.promt1(user_id)
        finally:
            pr.close()
        return promt1
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def contine_db(user_id):
    try:
        subject = subject_user()
        level = level_user()
        try:
            sub = subject.subject(user_id)
            lev = level.level(user_id)
        finally:
            level.close()
            subject.close()
        system_content = system(sub, lev)
        return system_content
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def add_contine_promt(r, user_id):
    try:
        add_promt = Add_promt()
        try:
            add_promt.add_pomt(r, user_id)
        finally:
            add_promt.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def mat(user_id):
    try:
        mat = 'Математика'
        add_subject = Add_subject()
        try:
            add_subject.add_subject(mat, user_id)
        finally:
            add_subject.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def rus(user_id):
    try:
        ru = 'Русский язык'
        add_ru = Add_subject()
        try:
            add_ru.add_subject(ru, user_id)
        finally:
            add_ru.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def chem(user_id):
    try:
        subject = 'Химия'
        add_ru = Add_subject()
        try:
            add_ru.add_subject(subject, user_id)
        finally:
            add_ru.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def level1(user_id):
    try:
        level = 'Новичок'
        add_level = Add_level()
        try:
            add_level.add_level(level, user_id)
        finally:
            add_level.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def level2(user_id):
    try:
        level = 'Базовый'
        add_level = Add_level()
        try:
            add_level.add_level(level, user_id)
        finally:
            add_level.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1


def level3(user_id):
    try:
        level = 'Профи'
        add_level = Add_level()
        try:
            add_level.add_level(level, user_id)
        finally:
            add_level.close()
    except Exception as e:
        error_gpt1 = error5
        logging.error(str(e))
        return error_gpt1