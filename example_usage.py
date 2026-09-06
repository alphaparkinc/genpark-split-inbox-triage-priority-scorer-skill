from client import SplitInboxTriagePriorityScorerClient

def main():
    client = SplitInboxTriagePriorityScorerClient()
    res = client.score_inbox_message_priority()
    print('Inbox Priority Scorer: ' + res['triage_id'] + ' -> ' + res['target_split_inbox'])
    print('Urgency: ' + res['urgency_tier'] + ' | SLA: ' + str(res['response_sla_deadline_hours']) + 'h')
    print('Dossier URL: ' + res['triage_dossier_url'])

if __name__ == '__main__':
    main()
