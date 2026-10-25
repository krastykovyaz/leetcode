# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 # Example 1:

# Input: 
numCourses = 2
prerequisites = [[1,0],[0,1], [1,0],[0,1]]
# prerequisites = [[1,0],[0,1]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

def course_shedule(num_course, courses):
    from collections import defaultdict
    graph = defaultdict(list)
    for course, prereq in courses:
        graph[prereq].append(course)
    visited = [0] * num_course # 0 - not visited, 1 - visited, 2 - visited twice (close)
    def dfs(course):
        if visited[course] == 1: # cycle occur
            return False
        if visited[course] == 2: # is worked
            return True
        visited[course] = 1
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        visited[course] = 2
        return True
    for c in range(num_course):
        if not dfs(c):
            return False
    return True
    
    


if __name__=='__main__':
    print(course_shedule(numCourses, prerequisites))

