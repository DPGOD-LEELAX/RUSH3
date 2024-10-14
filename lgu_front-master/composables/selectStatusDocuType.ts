export function selectStatusDocuType(){
    const status_options = [
        {
            "value":"in_progress",
            "display":"In Progress"
        },
        {
            "value":"completed",
            "display":"Completed"
        },
        {
            "value":"archived",
            "display":"Archived"
        },
        {
            "value":"disable",
            "display":"Disable"
        },
    ]
    const document_types = [
        "AIP",
        "Advisory",
        "Application Letter",
        "Authority to Travel",
        "COC-DPWH",
        "Certificate of No Pending Case",
        "Class Observation Plan",
        "Communications",
        "Conduct Research",
        "Daily Time Record (DTR)",
        "Designation Letter",
        "Disbursement Voucher",
        "Division Clearance",
        "ERF",
        "Endorsement of Transfer to other Division",
        "Fidelity Bond",
        "GSIS Maturity & Retirement Form",
        "Instructional Supervisory Plan",
        "Itinerary of Travel",
        "Job Order",
        "Leave Application",
        "Legal Documents"
    ]
    return{
        status_options,
        document_types
    }
}