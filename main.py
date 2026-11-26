#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for an
invented city to /output/entry.txt.

The city is Zibblewick, a place I made up for this entry: it rains warm
jam there instead of water, which is exactly the sort of small absurdity
a bored commuter at a rainy bus stop might smile at. The forecast keeps
the rhythm of a real broadcast ("light drizzle... 21C...") and bends it
toward the commuter's own morning: the bus is due, the coffee is still
warm, and for once the forecast is on their side.
"""

import os

# Version 2 of the entry line (revised: tighter middle, punchier ending
# that speaks directly to the commuter instead of hedging with a
# percentage; "bus due any minute and coffee still warm" is the concrete
# detail that makes Zibblewick feel like a place with a morning in it).
ENTRY = (
    "Zibblewick: light drizzle of warm jam, 21\u00b0C, bus due any minute "
    "and coffee still warm \u2014 today, the forecast is on your side."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
