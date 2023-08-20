def job_sequencing(jobs, max_deadline):

    jobs.sort(key=lambda x: x[2], reverse=True)

    sequence = [0] * max_deadline

    for job in jobs:

        slot = job[1] - 1
        while slot >= 0:
            if sequence[slot] == 0:
                sequence[slot] = job[0]
                break
            slot -= 1

    sequence = [job for job in sequence if job != 0]

    return sequence


jobs = [

    (1, 2, 100),
    (2, 1, 50),
    (3, 2, 60),
    (4, 1, 20),
    (5, 3, 70),
]
max_deadline = 3

result = job_sequencing(jobs, max_deadline)
print("Job sequence:", result)
