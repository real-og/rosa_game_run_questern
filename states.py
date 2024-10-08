from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    starting = State()
    entering_name = State()
    begin_waiting = State()

    task_1_running = State()
    task_2_running = State()
    task_3_running = State()
    task_4_running = State()
    task_5_running = State()

    task_1_solving = State()
    task_2_solving = State()
    task_3_solving = State()
    task_4_solving = State()
    task_5_solving = State()

    task_1_solved = State()
    task_2_solved = State()
    task_3_solved = State()
    task_4_solved = State()
    task_5_solved = State()

    task_4_solved_full = State()
    running_finish = State()

    secret_submitting = State()
    feedback_submitting = State()
    