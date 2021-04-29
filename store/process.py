from gc import callbacks

from django_logic import Process, Transition

from .condition import is_user, is_staff, is_planned, is_lock_available

LOCK_STATES = (
    ('maintenance', 'Under maintenance'),
    ('locked', 'Locked'),
    ('open', 'Open'),
    ('pause', 'Pause'),
)


def turn_on_alarm(lock, *args, **kwargs):
    print("Change any status here you like.")


class UserLockerProcess(Process):
    permissions = [is_user]
    transitions = [

        Transition(
            action_name='action_lock',
            sources=['open'],
            target='locked',
            callbacks=[
                turn_on_alarm
            ],
            side_effects=[
                turn_on_alarm
            ]
        ),
        Transition(
            action_name='action_unlock',
            sources=['locked'],
            target='open',
            callbacks=[
                turn_on_alarm
            ]
        )
    ]


class StaffLockerProcess(Process):
    permissions = [is_staff]
    all_states = [x for x, y in LOCK_STATES]

    transitions = [
        Transition(
            action_name='action_lock',
            sources=['open', 'maintenance'],
            target='locked',
            side_effects=[
                turn_on_alarm
            ],
            callbacks = [
                turn_on_alarm
            ]
        ),
        Transition(
            action_name='action_unlock',
            sources=['locked', 'maintenance'],
            target='open',
            side_effects=[
                turn_on_alarm
            ],
            callbacks= [
                turn_on_alarm
            ]
        ),
        Transition(
            action_name='action_maintain',
            sources=all_states,
            target='maintenance',
            side_effects=[
                turn_on_alarm
            ],
            callbacks=[
                turn_on_alarm
            ],
            conditions=[is_planned]
        )

    ]


class LockerProcess(Process):
    states = LOCK_STATES

    conditions = [is_lock_available]

    nested_processes = [
        StaffLockerProcess,
        UserLockerProcess,
    ]
