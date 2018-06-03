#!/bin/sh

cp podcast_info.json ../../podcast_connections/podcasts/fixtures/
cp similarities.json ../../podcast_connections/podcasts/fixtures/

cp guest_duration_podcast.json ../../podcast_connections/rankings/fixtures/
cp all_people.json ../../podcast_connections/rankings/fixtures/
# cp pr_top_hundred.json ../../podcast_connections/rankings/fixtures/
# cp hub_top_hundred.json ../../podcast_connections/rankings/fixtures/
# cp auth_top_hundred.json ../../podcast_connections/rankings/fixtures/
# cp deg_top_hundred.json ../../podcast_connections/rankings/fixtures/
# cp close_top_hundred.json ../../podcast_connections/rankings/fixtures/
# cp bt_top_hundred.json ../../podcast_connections/rankings/fixtures/
cp sorted_pr_dict.pkl ../../podcast_connections/six_degrees/

cp six_degrees.edgelist ../../podcast_connections/six_degrees/
cp podcast_id.pkl ../../podcast_connections/six_degrees/
cp correct_spellings.csv ../../podcast_connections/six_degrees/
