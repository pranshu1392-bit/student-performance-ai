def predict_marks(study_hours, attendance, assignments):
    m1 = 5      # study hours
    m2 = 0.3    # attendance
    m3 = 2      # assignments
    b = 10      # bias
    marks = (m1 * study_hours) + (m2 * attendance) + (m3 * assignments) + b
    return marks