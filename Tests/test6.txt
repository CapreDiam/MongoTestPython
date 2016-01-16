db.orders.aggregate( [ { $match : { provider: "~" } }, { $group: { _id: "$provider", sum: { $sum: "$price" } } } ] )
