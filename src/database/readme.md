for the player table, I think the best way to handle a new player would be to update the current row with to be inactive, then insert a new row with the current team and acive
should have lg too -- NBA, WNBA, G


MariaDB [nba_dev]> select * from player inner join team on team.team_id = player.team_id;
+-----------+--------------+------------+------+--------+------------+------+------------------------+------+
| player_id | player       | team_id    | lg   | active | team_id    | team | team_name              | lg   |
+-----------+--------------+------------+------+--------+------------+------+------------------------+------+
|      2544 | LeBron James | 1610612747 | lg   |      1 | 1610612747 | LAL  | Los Angeles Lakers     | lg   |
|    201144 | Mike Conley  | 1610612750 | lg   |      1 | 1610612750 | MIN  | Minnesota Timberwolves | lg   |
|    201567 | Kevin Love   | 1610612748 | lg   |      1 | 1610612748 | MIA  | Miami Heat             | lg   |
|    201572 | Brook Lopez  | 1610612749 | lg   |      1 | 1610612749 | MIL  | Milwaukee Bucks        | lg   |
+-----------+--------------+------------+------+--------+------------+------+------------------------+------+