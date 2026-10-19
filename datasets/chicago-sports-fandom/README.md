# Chicago sports fandom on Bluesky

401 Bluesky accounts tied to Chicago's eight major-league teams: the official and unofficial team accounts, beat writers, outlets, podcasters, fan pages, and fans. It is the seed list for a follower dataset (who follows which of these accounts). For educational purposes.

## Files

- `bluesky-accounts.csv` — one row per account, profile counts as of 2026-10-19.


## Coverage

| team | official | personnel | journalist | outlet | creator | fan_hub | fan | squat | total |
|---|---|---|---|---|---|---|---|---|---|
| Bears (NFL) |  | 2 | 22 | 2 | 24 | 11 |  | 1 | 62 |
| Bulls (NBA) |  | 1 | 9 | 3 | 9 | 14 | 14 |  | 50 |
| Cubs (MLB) |  |  | 14 | 5 | 19 | 13 | 1 | 1 | 53 |
| White Sox (MLB) | 1 | 2 | 6 | 6 | 18 | 5 | 7 |  | 45 |
| Blackhawks (NHL) | 1 |  | 11 | 3 | 7 | 4 | 15 | 2 | 43 |
| Fire (MLS) | 1 | 2 | 3 | 3 | 3 | 3 | 21 | 1 | 37 |
| Sky (WNBA) |  | 1 | 4 | 1 | 3 | 4 | 21 |  | 34 |
| Stars (NWSL) | 1 |  |  | 1 | 2 | 2 | 13 |  | 19 |
| Multiple |  |  | 32 | 9 | 7 | 4 | 6 |  | 58 |


## Columns

| column | what it holds |
|---|---|
| `handle` | Bluesky handle at collection time. Handles can change; `did` cannot |
| `did` | permanent account id (`did:plc:...`). Join on this |
| `display_name` | profile name, as written |
| `team` | primary team: `Bears`, `Bulls`, `Cubs`, `White Sox`, `Blackhawks`, `Fire`, `Sky`, `Stars`, or `Multiple` for accounts covering Chicago sports generally |
| `teams` | every team the account is assigned or names in its profile, `;`-separated. Blank for `Multiple` accounts that name no team |
| `sport` / `league` | of the primary team; `multiple` for `Multiple` |
| `category` | role, defined below |
| `followers` / `following` / `posts` | profile counts on 2026-10-19 |
| `created_at` | account creation date |
| `verified` | `True` if Bluesky shows a verification check |
| `found_via` | how the account first turned up: a starter pack (with its name), an account search (with the query), the follows of team hub accounts, or a search by a person's name |
| `starter_packs` | how many of the 47 starter packs used here list the account. A rough measure of how often fans recommend it |
| `notes` | context for unusual rows, quoting the profile where possible |
| `profile_url` | link to the profile |

### Categories

- `official` — run by the team or its owner. Only four exist: Chicago Fire FC and Chicago Stars FC (both verified), the Blackhawks-owned Rockford IceHogs, and `whitesox.com`, a domain handle with no posts.
- `personnel` — team staff, players, and former players whose profile states the connection (a Bulls PR head, the White Sox organist, Walter Payton's estate).
- `journalist` — reporters, broadcasters, editors, and producers at established outlets, including SB Nation and Bleacher Nation staff.
- `outlet` — brand accounts for media (CHGO Bears, Bleacher Nation, Tribune Sports, South Side Sox), plus four general Chicago news outlets.
- `creator` — independent bloggers, podcasters, and YouTubers focused on a team.
- `fan_hub` — fan-run accounts that act as a hub: news aggregators, bots, fan pages, supporters groups.
- `fan` — individual fans whose profile centers on one team.
- `squat` — team-named accounts with no content that people follow anyway (`chicagoblackhawks.bsky.social` has 1,550 followers and zero posts).


## Sources

- Bluesky public AppView API (`public.api.bsky.app`): `app.bsky.actor.searchActors`, `app.bsky.actor.getProfiles`, `app.bsky.graph.searchStarterPacks`, `app.bsky.graph.getStarterPack`, `app.bsky.graph.getList`, `app.bsky.graph.getFollows`, `app.bsky.graph.getFollowers`. Docs: https://docs.bsky.app/
- Starter packs curated by Bluesky users; the pack name for each account's first match is in `found_via`.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- Every account here is public, but these are real people. Use the list to study follow networks, not to single out individuals.
- Not affiliated with, endorsed by, or sponsored by any team, league, or Bluesky.
- Created in October 2026; profiles, handles, and counts will have changed by the time you use it.
