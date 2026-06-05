 from typing import List, Dict

class EnterpriseIQMock:
    @staticmethod
    def get_unresolved_communications() -> List[Dict[str, str]]:
        return [
            {
                "id": "msg_001",
                "source": "Teams Chat",
                "sender": "VP of Strategy",
                "content": "Urgent notice: We need approval on the revised Q3 launch budget changes by EOD today, otherwise our global supplier window completely closes."
            },
            {
                "id": "msg_002",
                "source": "Outlook Email",
                "sender": "External Vendor Logistics",
                "content": "Reviewing the delivery contract proposal. Please note we added a standard clause allowing an auto-markup of up to 12% for expedited shipping fees on rush orders."
            }
        ]

    @staticmethod
    def get_compliance_policy() -> str:
        return (
            "Corporate Procurement Guideline Section 4.2: Any vendor agreement containing "
            "automatic markups or expedited delivery surcharges exceeding 5% must be flagged "
            "immediately and rerouted directly to Corporate Legal Council for formal manual review."
        )

