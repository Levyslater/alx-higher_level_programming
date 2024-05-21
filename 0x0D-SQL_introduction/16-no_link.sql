-- lists all record of the table second_table of the database hbtn_0c_0
-- Don't list rows withot a name vale
-- Results shold display the score and the name(in this order)
-- Records should be listed by descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC, name ASC;
