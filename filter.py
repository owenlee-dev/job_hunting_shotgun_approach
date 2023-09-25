from pprint import pprint


def text_format(my_string):
    """Removes line breaks from a given string."""
    return my_string.replace('\n', ' ')


class JobListing:
    def __init__(self,
                employer_name,
                job_title,
                job_apply_link,
                job_description,
                job_country,
                employer_website="None",
                employer_company_type="None",
                apply_options="None",
                job_is_remote="None",
                job_city="None",
                job_required_experience="None",
                job_required_skills="None",
                job_job_title="None",
                job_posting_language="None",
                job_occupational_categories=None):
        self.employer_name = employer_name
        self.employer_website = employer_website
        self.employer_company_type = employer_company_type
        self.job_title = job_title
        self.job_apply_link = job_apply_link
        self.apply_options = apply_options
        self.job_description = job_description
        self.job_is_remote = job_is_remote
        self.job_country = job_country
        self.job_city = job_city
        self.job_required_experience = job_required_experience
        self.job_required_skills = job_required_skills
        self.job_job_title = job_job_title
        self.job_posting_language = job_posting_language
        self.job_occupational_categories = job_occupational_categories

    def __str__(self):
        apply_options_str = "\n".join([
            f"\tPublisher: {option['publisher']}, Link: {option['apply_link']}"
            for option in self.apply_options
        ])

        return (
            f"Employer Name: {self.employer_name}\n"
            f"Website: {self.employer_website}\n"
            f"Company Type: {self.employer_company_type}\n"
            f"Job Title: {self.job_title}\n"
            f"Apply Link: {self.job_apply_link}\n"
            f"Apply Options:\n{apply_options_str}\n"
            f"Description: {self.job_description}\n"
            f"Remote: {self.job_is_remote}\n"
            f"Country: {self.job_country}\n"
            f"City: {self.job_city}\n"
            f"Required Experience: {self.job_required_experience}\n"
            f"Skills: {self.job_required_skills}\n"
            f"Job Title: {self.job_job_title}\n"
            f"Posting Language: {self.job_posting_language}\n"
            f"Occupational Categories: {self.job_occupational_categories}"
        )

def filter_job_listings(job_listings_raw):
    job_listings=[]
    for listing_raw in job_listings_raw:
        # build listing object
        listing = JobListing(
            employer_name=listing_raw.get("employer_name","None"),
            employer_website=listing_raw.get("employer_website","None"),
            employer_company_type=listing_raw.get("employer_company_type","None"),
            job_title=listing_raw.get("job_title","None"),
            job_apply_link=listing_raw.get("job_apply_link","None"),
            apply_options=listing_raw.get("apply_options","None"),
            job_description=text_format(listing_raw.get("job_description","None")),
            job_is_remote=listing_raw.get("job_is_remote","None"),
            job_country=listing_raw.get("job_country","None"),
            job_city=listing_raw.get("job_city","None"),
            job_required_experience=listing_raw.get("job_required_experience","None"),
            job_required_skills=listing_raw.get("job_required_skills","None"),
            job_job_title=listing_raw.get("job_job_title","None"),
            job_posting_language=listing_raw.get("job_posting_language","None"),
            job_occupational_categories=listing_raw.get("job_occupational_categories","None"),
        )
        job_listings.append(listing)
    filterSeniorJobs(job_listings)
    filterNonEnglish(job_listings)

    # print all listings
    for listing in job_listings:
        print(listing)
    print(len(job_listings))     


# Function to filter out jobs that have the "Senior label or require more than 3 years of experience"
def filterSeniorJobs(job_listings):
    for listing in job_listings:
        if "senior" in listing.job_title.lower():
            job_listings.remove(listing);
        req_exp = listing.job_required_experience['required_experience_in_months'];
        if req_exp and req_exp > 36:
            job_listings.remove(listing);

def filterNonEnglish(job_listings):
    for listing in job_listings:
        if listing.job_posting_language != "en":
            job_listings.remove(listing)