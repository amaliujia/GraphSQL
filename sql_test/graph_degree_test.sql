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
SELECT out_degree, count(*) AS count
FROM (
  SELECT count(*) AS out_degree
  FROM GRAPH_TEST  AS A
  GROUP BY A.src_id
) AS degree_table
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
