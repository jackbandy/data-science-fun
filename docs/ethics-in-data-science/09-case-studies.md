# Famous Case Studies in Data Science Ethics

**[← Back to Course Homepage](../../index.html)**

🔴 *Chapter Status: in development. Each case has a short summary, but needs more description.*

Many professional fields develop various fables, myths, stories, etc. that serve as cautionary tales for practitioners.

* civil engineering - Tacoma Narrows Bridge
* psychology - Stanford / Milgram
* tech/politics/STS - bridges Long Island, New York

Although data science is in many ways still assembling its canon, there are some notable legends and case studies that I thought would be useful to compile here.

## Facebook's Voter Turnout Experiment (2010)

Facebook randomized an "I Voted" social message across roughly 61 million users during the 2010 U.S. midterm elections, and reported that the treatment produced somewhere around 340,000 additional votes [@bond_social_influence_2012].

TK.

* per-person effect was tiny, aggregate effect was potentially decisive
	* small effects at platform scale
* No consent and no debrief
* ability to influence turnout = ability to selectively influence turnout
* Lifecycle stage: intervention and reporting — [Chapter 5](05-ethics-in-reporting-decisions-solutions.md) prediction as intervention.

## Facebook's Emotional Contagion Experiment (2014)

For one week, researchers modified the emotional valence of News Feed content for 689,003 users without their knowledge, then measured the valence of those users' own subsequent posts [@kramer_emotional_contagion_2014].

*PNAS* published an editorial expression of concern [@verma_editorial_expression_2014]; James Grimmelmann wrote to the editor arguing the work fell squarely within human-subjects rules that had simply not been applied [@grimmelmann_letter_pnas_2014]; subsequent literature discussing corporate research ethics [@kahn_learning_2014; @boyd_untangling_2016].

TK. 

* Terms-of-service vs informed consent
* thousands of experiments, why did *this* one draw objections
* IRB obligations
* validity of findings

## Target's Pregnancy Prediction (2012)

Target built a pregnancy-prediction score from ordinary purchase histories — unscented lotion, certain supplements, oversized cotton balls — and used it to time marketing to expectant parents. The story reached a wide audience through Charles Duhigg's reporting, including a popular anecdote of a father who learned of his teenage daughter's pregnancy from Target's mailers [@duhigg_companies_secrets_2012].

TK.

* sensitive attributes inferred from non-sensitive data
	* inference as disclosure
* Target's reported response was to hide the inference (padding mailers with irrelevant coupons)

## Google Flu Trends (2008–2014)

Google Flu Trends (GFT) estimated influenza-like illness (ILI) from search query volume, initially tracking CDC surveillance data very closely, and appearing as a success story for big data. The original *Nature* paper reported roughly 97% accuracy against CDC data [@ginsberg_detecting_influenza_2009].

Lazer and colleagues' post-mortem, "The Parable of Google Flu," diagnoses the eventual failure as "big data hubris" [@lazer_google_flu_2014].

* GFT failed to predict **the 2009 spring H1N1 pandemic** — the model had been trained on seasonal flu and did not anticipate an off-season outbreak [@cook_assessing_gft_2011; @olson_reassessing_gft_2013].
* In **2011–2013** GFT consistently overestimated relative flu incidence, at one point predicting roughly twice as many doctors' visits as the CDC recorded [@lazer_google_flu_2014; @butler_google_flu_wrong_2013].
* A 2022 study found GFT was outperformed by the **recency heuristic** — predicting that this week's flu incidence equals last week's [@katsikopoulos_transparent_influenza_2022].

More TK.


* Lifecycle stage: understanding the data versus understanding the world — [Chapter 4](04-ethics-in-understanding.md).
* correlation with *search behavior*, not illness.
	* People searching "flu" or "flu symptoms" may be researching symptoms that resemble flu but are not flu [@olson_reassessing_gft_2013].
* Search behavior was itself changed by news coverage of flu season
	* Google began compensating for media-driven search spikes in fall 2013 [@harris_flu_tracker_sniffles_2014].
* The original model aggregated queries about *different health conditions*, inflating estimates [@lampos_advances_nowcasting_2015].
* Combining GFT with lagged CDC data, dynamically recalibrating, etc., [@lazer_google_flu_2014]
	* Further approaches [@preis_moat_adaptive_nowcasting_2014].[@lampos_advances_nowcasting_2015]

## Amazon's Résumé Screener (2014–2017)

Amazon built a tool to score job applicants' résumés from one to five stars, "much like shoppers rate products on Amazon."

By 2015 the team found it was systematically downgrading women for technical roles: it penalized applications containing the word "women's" (as in "women's chess club captain") and downgraded graduates of two all-women's colleges. The presumed cause was the training data — ten years of applications submitted to Amazon which were mostly from men. Amazon tried editing the model, but could not guarantee it would not find other proxies, and the project was abandoned by 2017 [@dastin_amazon_recruiting_2018].

TK.

* model did not include applicants' gender, did not need it
	* reconstructed the signal from proxies, which is the general problem — proxies in [Chapter 4](04-ethics-in-understanding.md).
* target variable: "who succeeded at this job" vs "who Amazon previously hired"
* Whack-a-mole as a bias mitigation strategy. Removing proxies one at a time does help with unknown ones (which is why the project was abandoned)
* Although often retold as "Amazon's hiring algorithm rejected women," Amazon's position was that recruiters looked at its recommendations (but the tool was never the sole basis for a decision)
	* paradox of automation
* Broader context: Amazon was not unusual in trying this
	* surveys of the algorithmic hiring vendor market [@bogen_rieke_help_wanted_2018]
	* vendors' own bias-mitigation claims [@raghavan_mitigating_bias_hiring_2020]

## The Tank Detector

* **The tank detector that learned the weather.** A neural network reportedly distinguished tanks from empty forest until someone noticed all the tank photographs were taken on cloudy days. Widely retold [@dreyfus_what_computers_still_cant_do_1992; @yudkowsky_ai_positive_negative_2008], and Gwern Branwen's survey of the tellings finds no verifiable original incident [@branwen_tank_legend_2011].
* Discussed in [Chapter 4](04-ethics-in-understanding.md).
* More TK
* Seems to be an urban legend?
* candidates — the "wolves versus huskies" snow-background classifier, the résumé screener that learned to prefer the name "Jared" and high-school lacrosse

::: {.content-visible when-format="html"}
## References
:::
