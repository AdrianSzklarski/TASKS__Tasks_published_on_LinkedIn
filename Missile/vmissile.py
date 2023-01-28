import math
import matplotlib.pyplot as plt


class Velocity:

    def __init__(self, r1, r2, r3, c1, c2, c3, r):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.r = r

    # Calculation of the speed of the 1st stage of the rocket
    def get_vel_I(self):
        tabI = []
        for step in range(1, 6):
            stage_I = round((self.r1 / step) * math.log(1 / (1 - self.c1)), 2)
            tabI.append(stage_I)
        return tabI[::-1]
        
    # Calculation of the speed of the 2nd stage of the rocket
    def get_vel_II(self):
        tab = self.get_vel_I()[4]
        tabII = []
        for step in range(1, 8):
            stage_II = round(((self.r2 / step) * math.log(1 / (1 - self.c2)) + tab), 2)
            tabII.append(stage_II)
        return tabII[::-1]

    # Calculation of the speed of the 3rd stage of the rocket
    def get_vel_III(self):
        tab = self.get_vel_II()[6]
        tabIII = []
        for step in range(1, 4):
            stage_III = round(((self.r3 / step) * math.log(1 / (1 - self.c3)) + tab) + 420, 2)
            tabIII.append(stage_III)
        return tabIII[::-1]

    # Gluing the charts together 
    def get_chart(self):
        tabI = self.get_vel_I()
        tabII = self.get_vel_II()
        tabIII = self.get_vel_III()

        for i in range(0, 15):
            return tabI + tabII + tabIII


if __name__ == '__main__':
    data = Velocity(35100, 5141, 1.033, 0.064, 0.582, 0.99, 2.4)
    print(data.get_chart())
    plt.title('Chart Velocity = f(Time) for Saturn V missile', fontsize=16)
    plt.xlabel('Time [min]', fontsize=16)
    plt.ylabel('V [m/s]', fontsize=16)
    plt.plot(data.get_chart())
    plt.show()
    
    
    
    
