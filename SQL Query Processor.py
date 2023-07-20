#!/usr/bin/python3
#
# Assignment2 Interface
#

import psycopg2   #--> need to un-comment this
import os
import sys
import math
# Donot close the connection inside this file i.e. do not perform openconnection.close()
# def RangeQuery(ratingsTableName, ratingMinValue, ratingMaxValue, openconnection):
#     pass


def RangeQuery(ratingsTableName, rating_min_value, rating_max_value, openconnection):
    cur = openconnection.cursor()

    cur.execute("SELECT COUNT(*) FROM RangeRatingsMetadata;")
    partitioning = cur.fetchone()[0]

    range_name = "RangeRatingsPart"
    robin_name = "RoundRobinRatingsPart"
    ranting_range_min = 0.0
    ranting_range_max = 5.0

    step = (ranting_range_max - ranting_range_min) / float(partitioning)

    rating_min_value = max(rating_min_value, 0.0)
    rating_max_value = min(rating_max_value, 5.0)

    if isinstance(rating_min_value, int) and rating_min_value != 0.0:
        ranting_range_min = rating_min_value - step
    else:
        ranting_range_min = math.floor(rating_min_value)

    range_partition_name_list = []
    while ranting_range_min <= rating_max_value and ranting_range_min != 5:
        cur.execute(
            "SELECT PartitionNum FROM RangeRatingsMetadata WHERE MinRating = %s AND MaxRating = %s;",
            (ranting_range_min, ranting_range_min + step)
        )
        partition_num = cur.fetchone()[0]
        range_partition_name_list.append(range_name + str(partition_num))
        ranting_range_min += step

    with open("RangeQueryOut.txt", 'a') as rangeFile:
        for partition_name in range_partition_name_list:
            cur.execute(
                "SELECT * FROM {} WHERE Rating >= %s AND Rating <= %s;".format(partition_name),
                (rating_min_value, rating_max_value)
            )
            partition_rows = cur.fetchall()
            for row in partition_rows:
                writeable_row = "{},{},{},{}".format(partition_name, row[0], row[1], row[2])
                rangeFile.write(writeable_row + '\n')

        for i in range(partitioning):
            robin_partition_name = robin_name + str(i)
            cur.execute(
                "SELECT * FROM {} WHERE Rating >= %s AND Rating <= %s;".format(robin_partition_name),
                (rating_min_value, rating_max_value)
            )
            round_robin_rows = cur.fetchall()
            for row in round_robin_rows:
                writeable_row = "{},{},{},{}".format(robin_partition_name, row[0], row[1], row[2])
                rangeFile.write(writeable_row + '\n')

def PointQuery(ratingsTableName, ratingValue, openconnection):
    cur = openconnection.cursor()

    # Get the number of partitions
    cur.execute("SELECT COUNT(*) FROM RangeRatingsMetadata;")
    particularizations = cur.fetchone()[0]

    # List to store partition names
    partition_name_list = []
    range_name = "RangeRatingsPart"
    robin_name = "RoundRobinRatingsPart"

    # Find the range partition names
    for i in range(0, particularizations):
        partition_name_list.append(range_name + str(i))

    # Find the round-robin partition names
    for i in range(0, particularizations):
        partition_name_list.append(robin_name + str(i))

    # Process partitions
    with open("PointQueryOut.txt", 'w') as pointFile:
        for partition_name in partition_name_list:
            cur.execute(
                "SELECT * FROM {} WHERE Rating = %s;".format(partition_name),
                (ratingValue,)
            )
            rows = cur.fetchall()

            # Write the rows to the output file
            for row in rows:
                writeable_row = "{},{},{},{}".format(partition_name, row[0], row[1], row[2])
                pointFile.write(writeable_row + '\n')


def writeToFile(filename, rows):
    f = open(filename, 'w')
    for line in rows:
        f.write(','.join(str(s) for s in line))
        f.write('\n')
    f.close()