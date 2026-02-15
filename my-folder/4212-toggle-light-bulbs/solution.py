class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()

        for bulb in bulbs:
            if bulb in on:
                on.remove(bulb)
            else:
                on.add(bulb)

        return sorted(list(on))
