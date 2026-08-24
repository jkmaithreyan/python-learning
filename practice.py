def summarize_shipments(records):
    total_by_region = {}
    delivered_by_region = {}
    unique_items = set()
    all_delivered = True

    for record in records:
        region = record["region"]

        # Total shipments by region
        if region in total_by_region:
            total_by_region[region] += 1
        else:
            total_by_region[region] = 1

        # Delivered shipments by region
        if region not in delivered_by_region:
            delivered_by_region[region] = 0

        if record["delivered"]:
            delivered_by_region[region] += 1
        else:
            all_delivered = False

        # Add unique items
        for item in record["items"]:
            unique_items.add(item)

    return {
        "total_by_region": total_by_region,
        "delivered_by_region": delivered_by_region,
        "unique_items": unique_items,
        "all_delivered": all_delivered
    }