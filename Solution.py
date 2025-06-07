# solution.py
def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    per_diem_rate = 50.00
    mileage_rate = 0.25
    receipt_threshold = 500.00
    receipt_base_rate = 1.0
    receipt_excess_rate = 0.5
    max_reimbursement = 5000.00
    short_trip_threshold = 1

    if trip_duration_days <= short_trip_threshold:
        return 0.00
    per_diem = per_diem_rate * trip_duration_days
    mileage = mileage_rate * miles_traveled
    receipts = (receipt_base_rate * total_receipts_amount if total_receipts_amount <= receipt_threshold
                else (receipt_base_rate * receipt_threshold) + (receipt_excess_rate * (total_receipts_amount - receipt_threshold)))
    total = min(per_diem + mileage + receipts, max_reimbursement)
    return round(total, 2)
