DROP TABLE IF EXISTS GRAPH_TEST;

CREATE TABLE GRAPH_TEST(src_id INT, dest_id INT, weight REAL);


INSERT INTO GRAPH_TEST VALUES(0, 1, 1);
INSERT INTO GRAPH_TEST VALUES(0, 2, 1);
INSERT INTO GRAPH_TEST VALUES(1, 2, 1);
INSERT INTO GRAPH_TEST VALUES(1, 3, 1);
INSERT INTO GRAPH_TEST VALUES(2, 3, 1);
INSERT INTO GRAPH_TEST VALUES(2, 5, 1);
INSERT INTO GRAPH_TEST VALUES(4, 1, 1);
INSERT INTO GRAPH_TEST VALUES(5, 2, 1);

CREATE VIEW out_degree_view AS
  SELECT A.src_id, count(*) AS out_degree
  FROM GRAPH_TEST  AS A
  GROUP BY A.src_id
  ORDER BY A.src_id ASC;


-- graph out degree
SELECT A.src_id, count(*) AS out_degree
FROM GRAPH_TEST  AS A
GROUP BY A.src_id
ORDER BY A.src_id ASC;

-- graph in degree
SELECT A.dest_id, count(*) AS in_degree
FROM GRAPH_TEST  AS A
GROUP BY A.dest_id
ORDER BY A.dest_id ASC;


-- graph in degree distribution
SELECT degree_table.in_degree, count(*) AS count
FROM (
  SELECT count(*) AS in_degree
  FROM GRAPH_TEST  AS A
  GROUP BY A.dest_id
) AS degree_table
GROUP BY in_degree
ORDER BY in_degree ASC;


-- graph out degree distribution
-- SELECT out_degree, count(*) AS count
-- FROM (
--   SELECT count(*) AS out_degree
--   FROM GRAPH_TEST  AS A
--   GROUP BY A.src_id
-- ) AS degree_table
-- GROUP BY out_degree
-- ORDER BY out_degree ASC;
SELECT out_degree, count(*) AS count
FROM out_degree_view
GROUP BY out_degree
ORDER BY out_degree ASC;

-- Degree distribution
SELECT degree, count(*) AS count
FROM (
  SELECT count(*) AS degree
  FROM GRAPH_TEST  AS A
  GROUP BY A.dest_id
  UNION ALL
  SELECT count(*) AS Degree
  FROM GRAPH_TEST  AS A
  GROUP BY A.src_id
) AS degree_table
GROUP BY degree
ORDER BY degree ASC;

DROP TABLE IF EXISTS GRAPH_TEST;
