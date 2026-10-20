"""A small ACM noticeboard for practicing Git."""

from club_data import EVENTS, MEMBERS


# Change this line on two branches to practice resolving a merge conflict.
WELCOME_MESSAGE = "Welcome to ACM!"


def seats_remaining(event):
    """Return the number of available seats for an event."""
    return max(0, event["capacity"] - event["registered"])


def show_events():
    print("\nUpcoming events")
    print("-" * 40)

    for event in EVENTS:
        print(f"\n{event['title']}")
        print(f"  When: {event['day']} at {event['time']}")
        print(f"  Where: {event['location']}")
        print(f"  Seats available: {seats_remaining(event)}")


def show_members():
    print("\nClub members")
    print("-" * 40)

    for member in MEMBERS:
        print(f"  - {member}")


def main():
    print(WELCOME_MESSAGE)
    show_events()
    show_members()


if __name__ == "__main__":
    main()
