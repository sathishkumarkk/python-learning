# The cost of one server per hour.
cost_per_hour = 0.51

# Compute the costs for one server.
cost_per_day = cost_per_hour * 24
cost_per_month = cost_per_day * 30

# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))