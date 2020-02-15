require 'pg'

conn = PG::connect(host: "localhost", dbname: "postgres")
res = conn.exec("select * from pg_stat_activity")

res.select {|item| item["backend_type"] == "checkpointer"}.each{|l|
	puts l
}

conn.finish
