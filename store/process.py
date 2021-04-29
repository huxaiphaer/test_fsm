from django_logic import Process, Action, Transition

from store.call_backs import turn_on_alarm
from store.condition import is_user, is_staff, is_planned, is_lock_available
from store.model_utils import Choices

LOCK_STATES = (
    ('maintenance', 'Under maintenance'),
    ('locked', 'Locked'),
    ('open', 'Open'),
)


class UserLockerProcess(Process):
    permissions = [is_user]
    transitions = [
        Action(
            action_name='action_refresh',
            sources=['open', 'locked']
        ),
        Transition(
            action_name='action_lock',
            sources=['open'],
            target='locked'
        ),
        Transition(
            action_name='action_unlock',
            sources=['locked'],
            target='open'
        )
    ]


class StaffLockerProcess(Process):
    permissions = [is_staff]
    all_states = [x for x, y in LOCK_STATES]

    transitions = [
        Transition(
            action_name='action_lock',
            sources=['open', 'maintenance'],
            target='locked'
        ),
        Transition(
            action_name='action_unlock',
            sources=['locked', 'maintenance'],
            target='open',
            callbacks=[
                turn_on_alarm
            ]
        ),
        Transition(
            action_name='action_maintain',
            sources=all_states,
            target='maintenance',
            conditions=[is_planned]
        ),

    ]


class LockerProcess(Process):
    states = LOCK_STATES

    conditions = [is_lock_available]

    nested_processes = [
        StaffLockerProcess,
        UserLockerProcess,
    ]