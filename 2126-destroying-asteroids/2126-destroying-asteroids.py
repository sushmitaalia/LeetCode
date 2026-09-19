class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if mass < i:
                return False
            mass += i
        return True