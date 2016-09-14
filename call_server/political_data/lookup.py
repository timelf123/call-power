from ..extensions import cache

from . import get_country_data

def locate_targets(location, campaign):
    """
    Locate targets for location for a given campaign.
    @return  list of target uids
    """

    if campaign.target_set:
        return [t.uid for t in campaign.target_set]
    else:
        country_code = campaign.get_country_code()
        country_data = get_country_data(country_code, cache=cache, api_cache='localmem')
        campaign_data = country_data.get_campaign_type(campaign.campaign_type)
        return campaign_data.get_targets_for_campaign(location, campaign)

