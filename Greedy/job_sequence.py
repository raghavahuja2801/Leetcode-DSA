def job_sequencing(jobs):
    """
    Find the maximum profit job sequence where jobs can be completed before their deadlines.
    
    Parameters:
        jobs (list[tuple]): A list of tuples where each tuple contains (job_id, profit, deadline).
    
    Returns:
        list: The sequence of jobs for maximum profit.
    """
    jobs.sort(key=lambda x: x[1], reverse=True)  # Sort jobs by profit in descending order
    
    max_deadline = max(job[2] for job in jobs)  # Find maximum deadline
    slots = [-1] * (max_deadline + 1)  # Slots to store job IDs
    
    total_profit = 0
    job_sequence = []

    for job in jobs:
        job_id, profit, deadline = job
        for t in range(deadline, 0, -1):  # Find a free slot before the deadline
            if slots[t] == -1:
                slots[t] = job_id  # Assign job to slot
                total_profit += profit
                job_sequence.append(job_id)
                break
    
    return job_sequence, total_profit

# Example usage
jobs = [("a", 50, 2), ("b", 60, 1), ("c", 70, 2), ("d", 30, 1)]
job_sequence, total_profit = job_sequencing(jobs)
print("Job sequence:", job_sequence)
print("Total profit:", total_profit)
