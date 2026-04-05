class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        in_degree = [0 for _ in range(numCourses)]
        course_graph = {course : [] for course in range(numCourses)}


        # a -> b edge indicates that a is prereq for b
        for course, prereq in prerequisites:
            
            course_graph[prereq].append(course)
            in_degree[course] += 1
        
        print("course graph", course_graph)
        print("in degree" , in_degree)

        queue = [ idx for idx, num_prereqs in enumerate(in_degree) if num_prereqs == 0]

        print("courses with 0 prereqs:", queue)

        courses_processed = 0
        while queue:
            course = queue.pop()
            courses_processed += 1
            for next_course in course_graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return courses_processed == numCourses
        