
from django_logic import Process, Transition

from store import call_backs


COOPERATION_PARTNER_STATE_REGISTERED = 'Registered'
COOPERATION_PARTNER_STATE_ON_HOLD = 'On hold'
COOPERATION_PARTNER_STATE_APPROVED = 'Approved'
COOPERATION_PARTNER_STATE_REJECTED = 'Rejected'
COOPERATION_PARTNER_STATE_EXPIRED = 'Registered (expired)'

COOPERATION_PARTNER_STATE_CHOICES = (
    (COOPERATION_PARTNER_STATE_REGISTERED,
     COOPERATION_PARTNER_STATE_REGISTERED),
    (COOPERATION_PARTNER_STATE_ON_HOLD,
     COOPERATION_PARTNER_STATE_ON_HOLD),
    (COOPERATION_PARTNER_STATE_APPROVED,
     COOPERATION_PARTNER_STATE_APPROVED),
    (COOPERATION_PARTNER_STATE_REJECTED,
     COOPERATION_PARTNER_STATE_REJECTED),
    (COOPERATION_PARTNER_STATE_EXPIRED,
     COOPERATION_PARTNER_STATE_EXPIRED),
)


class CooperationPartnerProcess(Process):

    states = COOPERATION_PARTNER_STATE_CHOICES

    transitions = [
        Transition(
            action_name='action_verify_account',
            sources=[COOPERATION_PARTNER_STATE_REGISTERED,
                     COOPERATION_PARTNER_STATE_EXPIRED],
            target=COOPERATION_PARTNER_STATE_ON_HOLD,
            side_effects=[
                call_backs.verify_account
            ],
            callbacks=[
                call_backs.verify_account
            ]
        ),

        Transition(
            action_name='action_approve_account',
            sources=[COOPERATION_PARTNER_STATE_ON_HOLD,
                     COOPERATION_PARTNER_STATE_REJECTED],
            target=COOPERATION_PARTNER_STATE_APPROVED,
            side_effects=[
                call_backs.approve_account
            ]
        ),
        Transition(
            action_name='action_reject_account',
            sources=[
                COOPERATION_PARTNER_STATE_ON_HOLD,
                COOPERATION_PARTNER_STATE_APPROVED
            ],
            target=COOPERATION_PARTNER_STATE_REJECTED,
            side_effects=[
                call_backs.reject_account
            ]
        ),

    ]
