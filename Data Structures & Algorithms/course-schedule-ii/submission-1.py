class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0 for _ in range(numCourses)]
        course_graph = {course : [] for course in range(numCourses)}

        # a -> b edge indicates that a is prereq for b
        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
            in_degree[course] += 1

        queue = [ idx for idx, num_prereqs in enumerate(in_degree) if num_prereqs == 0]
        ordering = []

        courses_processed = 0
        while queue:
            course = queue.pop()
            courses_processed += 1
            ordering.append(course)
            for next_course in course_graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        if courses_processed == numCourses:
            return ordering
        return []