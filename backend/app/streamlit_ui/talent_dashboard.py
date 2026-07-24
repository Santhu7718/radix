import streamlit as st
from app.services.talent_service import load_companies, compare_candidate


def show_talent_dashboard():

    st.header("🎯 Talent Check")
    st.caption("Analyze candidate readiness for top companies")

    companies = load_companies()

    company = st.selectbox(
        "🏢 Select Company",
        list(companies.keys())
    )

    if st.button("🚀 Analyze Candidate", use_container_width=True):

        result = compare_candidate(company)

        score = result["score"]
        matched = result["matched"]
        missing = result["missing"]
        required = result["required"]

        st.divider()

        # ==========================
        # Score Cards
        # ==========================

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("🎯 Readiness", f"{score}%")
        c2.metric("✅ Matched", len(matched))
        c3.metric("❌ Missing", len(missing))
        c4.metric("📚 Required", len(required))

        st.progress(score / 100)

        if score >= 85:
            st.success("🟢 Excellent Match")
        elif score >= 70:
            st.info("🔵 Good Match")
        elif score >= 50:
            st.warning("🟡 Average Match")
        else:
            st.error("🔴 Needs Improvement")

        st.divider()

        # ==========================
        # Suitable Roles
        # ==========================

        st.subheader("💼 Suitable Roles")

        cols = st.columns(2)

        for i, role in enumerate(result["roles"]):
            cols[i % 2].success(role)

        st.divider()

        # ==========================
        # Skills
        # ==========================

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matching Skills")

            if matched:
                for skill in matched:
                    st.success(f"✔ {skill}")
            else:
                st.warning("No matching skills.")

        with right:

            st.subheader("❌ Missing Skills")

            if missing:
                for skill in missing:
                    st.error(f"✖ {skill}")
            else:
                st.success("No missing skills!")

        st.divider()

        # ==========================
        # Career Verdict
        # ==========================

        st.subheader("🎯 Career Assessment")

        if score >= 85:

            st.success(
                f"""
### Ready to Apply

You have an excellent skill match for **{company}**.

Recommended Action:
- Apply immediately
- Focus on interview preparation
"""
            )

        elif score >= 70:

            st.info(
                f"""
### Nearly Ready

Improve a few missing skills before applying.
"""
            )

        elif score >= 50:

            st.warning(
                f"""
### Moderate Match

Spend some time improving the highlighted skills.
"""
            )

        else:

            st.error(
                f"""
### Not Ready Yet

Build stronger fundamentals before applying.
"""
            )

        st.divider()

        # ==========================
        # Learning Roadmap
        # ==========================

        st.subheader("📚 Recommended Learning Roadmap")

        roadmap = missing[:8]

        if roadmap:

            cols = st.columns(2)

            for i, skill in enumerate(roadmap):

                week = (i // 2) + 1

                cols[i % 2].info(
                    f"**Week {week}**\n\n• {skill}"
                )

        st.divider()

        # ==========================
        # Skill Distribution
        # ==========================

        st.subheader("📈 Skill Distribution")

        st.write(f"**Matched Skills:** {len(matched)}")
        st.progress(len(matched) / len(required))

        st.write(f"**Missing Skills:** {len(missing)}")
        st.progress(len(missing) / len(required))

        st.divider()

        # ==========================
        # Expanders
        # ==========================

        with st.expander("📋 View All Required Skills"):

            for skill in required:
                st.write("•", skill)

        with st.expander("📄 Full Analysis Data"):

            st.json(result)