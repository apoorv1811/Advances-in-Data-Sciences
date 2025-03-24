import streamlit as st

# Set page configuration
st.set_page_config(page_title="Crash Course in Causality", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Exam Preparation", "Quiz"])

if page == "Quiz":
    st.title("Causality Quiz")
    st.write("Test your knowledge on causal inference and reasoning!")

    questions = [
        {
            "question": "Which of the following are necessary for establishing causality?",
            "options": ["Temporal precedence", "Correlation between variables", "Absence of any third variables", "A plausible mechanism"],
            "correct": ["Temporal precedence", "Correlation between variables", "A plausible mechanism"],
            "explanation": "- Temporal precedence: The cause must occur before the effect.  \n- Correlation between variables: A necessary (but not sufficient) component of causality.  \n- Absence of any third variables: Incorrect, as we aim to control for confounders, not eliminate all.  \n- A plausible mechanism: Supports the logical connection between cause and effect."
        },
        {
            "question": "Which statements about confounding variables are true?",
            "options": ["Confounders can create a spurious association between two variables.", "A confounder is always a mediator.", "Controlling for confounders helps isolate the causal relationship.", "Confounders are irrelevant in randomized controlled trials."],
            "correct": ["Confounders can create a spurious association between two variables.", "Controlling for confounders helps isolate the causal relationship."],
            "explanation": "- Confounders can make it appear that a relationship exists when it doesn't.  \n- A confounder is not a mediator; they serve different roles.  \n- Controlling for confounders reduces bias.  \n- RCTs aim to balance confounders but do not make them irrelevant."
        },
        {
            "question": "What is a counterfactual?",
            "options": ["A hypothetical alternative to what actually happened", "A misleading statistic", "A key component of causal inference", "An error in observational research"],
            "correct": ["A hypothetical alternative to what actually happened", "A key component of causal inference"],
            "explanation": "- Counterfactuals define what would happen in alternate scenarios.  \n- They form the foundation for causal reasoning.  \n- Not misleading or erroneous by nature; they are vital for inference."
        },
        {
            "question": "Which of the following can introduce bias in observational studies?",
            "options": ["Selection bias", "Confounding variables", "Random sampling", "Measurement error"],
            "correct": ["Selection bias", "Confounding variables", "Measurement error"],
            "explanation": "- Selection bias and confounding distort results.  \n- Measurement error can skew relationships.  \n- Random sampling helps reduce bias."
        },
        {
            "question": "Which statements are true about correlation and causation?",
            "options": ["Correlation always implies causation", "Reverse causality may occur", "Chance may produce correlation", "Correlation is necessary but not sufficient for causation"],
            "correct": ["Reverse causality may occur", "Chance may produce correlation", "Correlation is necessary but not sufficient for causation"],
            "explanation": "- Correlation does not guarantee causality.  \n- The effect could cause the cause (reverse causality).  \n- Random patterns may yield correlations."
        },
        {
            "question": "What are characteristics of a good instrumental variable?",
            "options": ["It affects the treatment", "It affects the outcome directly", "It is unrelated to confounders", "It only affects the outcome through the treatment"],
            "correct": ["It affects the treatment", "It is unrelated to confounders", "It only affects the outcome through the treatment"],
            "explanation": "- IVs must influence treatment.  \n- They cannot affect the outcome directly.  \n- Independence from confounders is essential."
        },
        {
            "question": "Which techniques are used to reduce confounding in observational studies?",
            "options": ["Matching", "Propensity score adjustment", "Random sampling", "Stratification"],
            "correct": ["Matching", "Propensity score adjustment", "Stratification"],
            "explanation": "- These techniques help equate groups and reduce bias.  \n- Random sampling doesn't directly adjust for confounding."
        },
        {
            "question": "Which of the following are assumptions of the potential outcomes framework?",
            "options": ["SUTVA", "Ignorability", "Random measurement error", "No missing data"],
            "correct": ["SUTVA", "Ignorability"],
            "explanation": "- SUTVA and Ignorability are essential to infer causality.  \n- Measurement error and missing data are technical challenges, not core assumptions."
        },
        {
            "question": "What can causal diagrams (DAGs) be used for?",
            "options": ["Identifying confounders", "Visualizing data trends", "Guiding variable adjustment", "Highlighting spurious correlations"],
            "correct": ["Identifying confounders", "Guiding variable adjustment"],
            "explanation": "- DAGs help determine what to adjust for.  \n- They model causal paths, not general data trends."
        },
        {
            "question": "Which are examples of post-treatment bias?",
            "options": ["Adjusting for a mediator", "Randomizing treatment assignment", "Conditioning on a post-treatment collider", "Ignoring confounders"],
            "correct": ["Adjusting for a mediator", "Conditioning on a post-treatment collider"],
            "explanation": "- Adjusting for variables affected by treatment biases results.  \n- Randomization avoids bias, not causes it."
        },
        {
            "question": "Which features make RCTs reliable for causal inference?",
            "options": ["Randomization", "Controlled interventions", "Generalizability", "Temporal ordering"],
            "correct": ["Randomization", "Controlled interventions", "Temporal ordering"],
            "explanation": "- RCTs ensure timing, intervention control, and balance.  \n- Generalizability is sometimes limited in RCTs."
        },
        {
            "question": "What is true about natural experiments?",
            "options": ["They use as-if random assignment", "They always mimic RCTs", "They can identify causal effects", "They don't require control variables"],
            "correct": ["They use as-if random assignment", "They can identify causal effects"],
            "explanation": "- External events may simulate experiments.  \n- Not all natural experiments are perfect."
        },
        {
            "question": "Which statements about counterfactuals are true?",
            "options": ["They are observable for all units", "They form the basis of causal inference", "They represent hypothetical scenarios", "They can always be tested"],
            "correct": ["They form the basis of causal inference", "They represent hypothetical scenarios"],
            "explanation": "- Counterfactuals describe what didn't happen.  \n- Only one outcome is observed per unit."
        },
        {
            "question": "What does 'no causation without manipulation' imply?",
            "options": ["Causal claims need interventions", "Observational studies are invalid", "Manipulations reveal effects", "Causal reasoning requires change"],
            "correct": ["Causal claims need interventions", "Manipulations reveal effects", "Causal reasoning requires change"],
            "explanation": "- This phrase emphasizes active change or hypothetical manipulation to infer causality."
        },
        {
            "question": "Which are common pitfalls in causal inference?",
            "options": ["Mistaking correlation for causation", "Controlling for colliders", "Using invalid instruments", "Ensuring SUTVA holds"],
            "correct": ["Mistaking correlation for causation", "Controlling for colliders", "Using invalid instruments"],
            "explanation": "- These lead to bias or incorrect conclusions.  \n- Ensuring SUTVA holds is not a pitfall but a necessary step."
        }
    ]

    user_answers = {}
    unanswered_questions = []

    for idx, q in enumerate(questions):
        st.subheader(f"Question {idx + 1}: {q['question']}")
        user_answers[idx] = []
        for option in q["options"]:
            selected = st.checkbox(option, key=f"q{idx}_{option}")
            if selected:
                user_answers[idx].append(option)

    if st.button("Submit Quiz"):
        unanswered_questions = [idx for idx in user_answers if not user_answers[idx]]

        if unanswered_questions:
            st.warning("Please attempt all questions before submitting the quiz.")
        else:
            total_score = 0
            max_score = len(questions) * 4

            st.subheader("Quiz Results")

            for idx, q in enumerate(questions):
                st.write(f"**Question {idx + 1}: {q['question']}**")
                if set(user_answers[idx]) == set(q["correct"]):
                    st.success("Correct! 🎉 (+4 marks)")
                    total_score += 4
                else:
                    st.error(f"Incorrect. The correct answer is: {', '.join(q['correct'])} (+0 marks)")

                st.markdown("**Explanation:** " + q["explanation"].replace("\n", "  \n"))
                st.write("---")

            st.subheader("Final Score")
            st.write(f"You secured **{total_score}** out of **{max_score}** marks.")



elif page == "Exam Preparation":
    st.title("Exam Preparation: Crash Course in Causality")
    st.write("### Chapter 1: Introduction to Causality")
    st.markdown("""
    Causality lies at the heart of scientific reasoning. It is the pursuit of understanding not just whether two variables are related, but whether one actually brings about a change in the other. This distinction is crucial for meaningful research, effective policy, and everyday decision-making. Whereas correlation describes a statistical association between variables, causation implies a directional, explanatory relationship—"X causes Y."
    """)

    st.write("### Chapter 2: Correlation vs. Causation")
    st.markdown("""
    One of the most fundamental distinctions in research is that between correlation and causation. Correlation means two variables move together—when one increases, the other might also increase (positive correlation) or decrease (negative correlation). However, this pattern alone does not mean one causes the other.

    For example, ice cream sales and drowning rates might rise together in summer. This correlation is due to a third variable—temperature—not a causal link between the two. This illustrates why establishing causation requires more rigorous tools.

    To claim causation, we typically need three conditions:
    1. **Temporal Precedence:** The cause must precede the effect in time.
    2. **Covariation:** The cause and effect must be associated.
    3. **Elimination of Alternative Explanations:** Other possible explanations must be ruled out, especially confounding variables.
    """)

    st.write("### Chapter 3: Confounding and Bias")
    st.markdown("""
    **Confounding variables** are third variables that influence both the independent variable (cause) and the dependent variable (effect). They can create misleading associations and are a major obstacle to identifying true causal relationships.

    Example: Suppose we find a correlation between carrying lighters and lung cancer. Does carrying a lighter cause cancer? Likely not. The confounding variable—smoking—is associated with both the lighter and the disease.

    Other forms of bias include:
    - **Selection Bias:** Occurs when the sample is not representative.
    - **Measurement Error:** When variables are inaccurately recorded.
    - **Post-Treatment Bias:** When you condition on variables that are affected by the treatment, distorting the causal pathway.

    To mitigate these biases, researchers use techniques like matching, stratification, and regression adjustment.
    """)

    st.write("### Chapter 4: Counterfactuals and Potential Outcomes")
    st.markdown("""
    The **counterfactual** framework asks: What would have happened to the same unit if it had received a different treatment? Since we can never observe both outcomes for the same unit, we infer the unobserved (counterfactual) from others who are similar.

    This leads to the **Potential Outcomes Framework**, which forms the basis for modern causal inference. Each individual has two potential outcomes: one under treatment and one under control. The causal effect is the difference between these.

    However, we only observe one outcome per individual. This challenge is known as the **fundamental problem of causal inference**.

    To estimate average effects, we need assumptions like:
    - **Ignorability (Unconfoundedness):** Treatment assignment is independent of potential outcomes, given covariates.
    - **SUTVA (Stable Unit Treatment Value Assumption):** One person’s treatment doesn't affect another’s outcome, and treatments are consistent.
    """)

    st.write("### Chapter 5: Randomized Controlled Trials (RCTs)")
    st.markdown("""
    RCTs are the gold standard for establishing causality. By randomly assigning treatment, RCTs aim to balance confounding variables across treatment and control groups.

    **Key features of RCTs:**
    - **Randomization:** Eliminates confounding by design.
    - **Temporal Ordering:** Ensures cause precedes effect.
    - **Clear Intervention:** Treatment is known and controlled.

    Limitations of RCTs include ethical concerns, high cost, and limited generalizability. They are not always feasible, which is why observational studies and natural experiments remain essential.
    """)

    st.write("### Chapter 6: Observational Studies and Natural Experiments")
    st.markdown("""
    When RCTs are impractical, researchers turn to **observational data**. Here, treatment assignment is not controlled by the researcher, so we must carefully control for confounding.

    **Natural Experiments** occur when external factors (e.g., policy changes, natural disasters) assign treatment in a way that is "as if random." These provide quasi-experimental conditions useful for causal inference.

    Analytical techniques in observational studies include:
    - **Matching:** Pairing treated and untreated units with similar covariates.
    - **Propensity Score Methods:** Estimating the probability of treatment to balance groups.
    - **Stratification and Regression Adjustment:** Controlling for confounding statistically.
    """)

    st.write("### Chapter 7: Causal Diagrams (Directed Acyclic Graphs - DAGs)")
    st.markdown("""
    **Causal diagrams**, or DAGs, are graphical tools used to visualize relationships between variables. They consist of:
    - **Nodes:** Representing variables
    - **Directed Arrows:** Representing causal influence
    - **No Cycles:** Ensures the graph is acyclic (no feedback loops)

    DAGs help identify confounders, mediators, and colliders, guiding which variables to control for in analysis. Conditioning on colliders or post-treatment variables can introduce bias, which DAGs help avoid.
    """)

    st.write("### Chapter 8: Instrumental Variables (IV)")
    st.markdown("""
    When unobserved confounding is present, **instrumental variables** offer a solution. An IV affects the treatment but has no direct path to the outcome, except through the treatment.

    **Conditions for a valid instrument:**
    1. **Relevance:** The IV must affect the treatment.
    2. **Exclusion Restriction:** The IV affects the outcome only via the treatment.
    3. **Independence:** The IV is not related to unmeasured confounders.

    Example: Using distance to college as an IV for education level when estimating the causal effect of education on earnings.
    """)

    st.write("### Chapter 9: Interventions and the Logic of Manipulation")
    st.markdown("""
    Causality is fundamentally about **interventions**. Judea Pearl’s "do-calculus" formalizes the idea of manipulating variables and observing the consequences.

    **"No causation without manipulation"** reflects the idea that to establish causation, we must imagine or perform interventions. Even in observational data, researchers simulate interventions through statistical control and counterfactual reasoning.
    """)

    st.write("### Chapter 10: Common Pitfalls and Misconceptions")
    st.markdown("""
    - **Mistaking correlation for causation**
    - **Controlling for mediators or colliders**
    - **Using inappropriate instruments**
    - **Ignoring assumptions (e.g., SUTVA, ignorability)**

    Causal inference requires a careful blend of theory, methodology, and domain expertise. It is not purely statistical—it requires judgment and justification.
    """)

    st.write("### Conclusion")
    st.markdown("""
    Causal reasoning enables us to answer the most important questions: What causes what? What would happen if we changed something? Understanding causality equips us with tools not just for analysis, but for action. From policy-making to medicine to machine learning, causality underpins meaningful insight and responsible decision-making.

    By mastering the principles outlined in this crash course—confounding, counterfactuals, DAGs, interventions, and experimental design—you will be better equipped to both critique and conduct causal research.
    """)

    st.success("Use this guide to understand key causal concepts and prepare for your exam!")
