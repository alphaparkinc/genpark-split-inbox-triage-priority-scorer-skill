class SplitInboxTriagePriorityScorerClient:
    def score_inbox_message_priority(self, sender_email='investor@sequoia.com', subject='Urgent: Q3 Board Meeting Follow-up', has_attachments=True):
        is_vip = 'investor' in sender_email or 'vip' in sender_email
        return {
            'triage_id': 'inb_trg_7719',
            'sender_email': sender_email,
            'subject': subject,
            'target_split_inbox': 'VIP_INVESTORS' if is_vip else 'GENERAL_INBOX',
            'urgency_tier': 'P0_IMMEDIATE_ACTION' if is_vip else 'P2_NORMAL',
            'response_sla_deadline_hours': 2 if is_vip else 24,
            'automated_quick_reply_suggested': True,
            'triage_dossier_url': 'https://productivity.developer.genpark.ai/superhuman/triage/inb_trg_7719.json'
        }
