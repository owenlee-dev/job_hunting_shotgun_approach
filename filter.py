from pprint import pprint


def text_format(my_string):
    """Removes line breaks from a given string."""
    return my_string.replace("\n", " ")


class JobListing:
    def __init__(
        self,
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
    ):
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

    def __str__(self):
        apply_options_str = "\n".join(
            [
                f"\tPublisher: {option['publisher']}, Link: {option['apply_link']}"
                for option in self.apply_options
            ]
        )

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
        )


def filter_job_listings(job_listings_raw):
    job_listings = []
    for i in range(len(job_listings_raw)):
        # break;
        listing = JobListing(
            employer_name=job_listings_raw[i]["employer_name"],
            employer_website=job_listings_raw[i]["employer_website"],
            employer_company_type=job_listings_raw[i]["employer_company_type"],
            job_title=job_listings_raw[i]["job_title"],
            job_apply_link=job_listings_raw[i]["job_apply_link"],
            apply_options=job_listings_raw[i]["apply_options"],
            job_description=text_format(
                job_listings_raw[i]["job_description"],
            ),
            job_is_remote=job_listings_raw[i]["job_is_remote"],
            job_country=job_listings_raw[i]["job_country"],
            job_city=job_listings_raw[i]["job_city"],
            job_required_experience=job_listings_raw[i]["job_required_experience"],
            job_required_skills=job_listings_raw[i]["job_required_skills"],
            job_job_title=job_listings_raw[i]["job_job_title"],
            job_posting_language=job_listings_raw[i]["job_posting_language"],
        )
        job_listings.append(listing)

    filterSeniorJobs(job_listings)
    filterNonEnglish(job_listings)
    for listing in job_listings:
        print(f"{listing.employer_name} , {listing.job_title} , {listing.job_posting_language}")
    return job_listings


# Function to filter out jobs that have the "Senior label or require more than 3 years of experience"
def filterSeniorJobs(job_listings):
    to_remove=[]
    for listing in job_listings:
        req_exp = listing.job_required_experience["required_experience_in_months"]
        if "senior" in listing.job_title.lower():
            to_remove.append(listing)
        elif req_exp and req_exp > 36:
            to_remove.append(listing)

    for listing in to_remove:
        job_listings.remove(listing)


def filterNonEnglish(job_listings):
    for listing in job_listings:
        if listing.job_posting_language != "en":
            job_listings.remove(listing)
