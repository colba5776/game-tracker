use gametrackerdb;

/* Apply constraints to the PlaythroughAchivement table. */
alter table playthroughachievement
add constraint statusCheck check (achievementStatus in ('Complete','Incomplete'));

/* Apply constraints to the Rating table. */
alter table rating
add constraint valueCheck check (ratingValue >= 1 AND ratingValue <= 10);

/* Apply constraints to the Playthrough table. */
alter table playthrough
add constraint endDateCheck check (playthroughEndDate >= playthroughStartDate);