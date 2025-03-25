# Last updated: 3/26/2025, 1:50:49 AM
class Solution:
    def countLineIntersections(self, coordinates):
        lines = 0
        overlap = 0
        for _, is_start in coordinates:
            if is_start == 0:
                overlap -= 1
            else:
                overlap += 1
            if overlap == 0:
                lines += 1
        return lines >= 3

    def checkValidCuts(self, n, rectangles):
        y_coordinates = []
        x_coordinates = []
        
        for rectangle in rectangles:
            x_coordinates.append((rectangle[0], 1))  
            x_coordinates.append((rectangle[2], 0))  
            y_coordinates.append((rectangle[1], 1))  
            y_coordinates.append((rectangle[3], 0))  
        
        x_coordinates.sort()
        y_coordinates.sort()

        return self.countLineIntersections(x_coordinates) or self.countLineIntersections(y_coordinates)





        