import requests
import json
def teamFinder(event, circus):
    def ezMatch(matchStr):
        if (matchStr == "f"):
            return "finals"
        elif (matchStr == "sf"):
            return "semifinals"
        elif (matchStr == "qf"):
            return "quarterfinals"
        elif (matchStr == "qm"):
            return "qualifications"
        else:
            return "{match type not found}"

    event #event (can be found on TBA)
    team = "frc254" #your team. In this case, frc254
    comparedNum = circus #team number imported
    compared = "frc" + str(circus) #team number with "frc" in front (required for TBA API)
    wap = [] #list that is later written to and printed from
    i = 0


    headers = {
        'Accept': 'application/json',
        'User-Agent': 'TBA-TeamComparer'
    }

    params = {
        'event': event,
        'X-TBA-Auth-Key': '[Dont steal my key!]'
    }

    matches_url = f'https://www.thebluealliance.com/api/v3/event/{event}' + '/matches'
    response = requests.get(matches_url, headers=headers, params=params)
    matches_data = json.loads(response.content.decode('utf-8'))

    team_254_matches = [match for match in matches_data if
                        team in match["alliances"]["blue"]["team_keys"] or team in match["alliances"]["red"][
                            "team_keys"]]
    compared_matches = [match for match in matches_data if
                        compared in match["alliances"]["blue"]["team_keys"] or compared in match["alliances"]["red"][
                            "team_keys"]]

    matches_together = [match for match in team_254_matches if
                        compared in match["alliances"]["blue"]["team_keys"] or compared in match["alliances"]["red"][
                            "team_keys"]]

    def staple(match):
        if [match for match in matches_data if team in match["alliances"]["blue"]["team_keys"]]:
            if [match for match in matches_data if compared in match["alliances"]["blue"]["team_keys"]]:
                return "partner"
            elif [match for match in matches_data if team in match["alliances"]["red"]["team_keys"]]:
                return "opponent"
        elif [match for match in matches_data if team in match["alliances"]["red"]["team_keys"]]:
            if [match for match in matches_data if compared in match["alliances"]["blue"]["team_keys"]]:
                return "opponent"
            elif [match for match in matches_data if compared in match["alliances"]["red"]["team_keys"]]:
                return "partner"

    print(f"Matches for 254 && {comparedNum} @ {event}")
    for match in matches_together:
        wap.append(f"Match {match['match_number']}: {staple(match)} {ezMatch(match['comp_level'])} match between {match['alliances']['blue']['team_keys']} and {match['alliances']['red']['team_keys']}")
        i = i+1
    a = len(wap)-1
    while a >= 0:
        print(wap[a])
        a -= 1


teamFinder("2023cada", 1678)
