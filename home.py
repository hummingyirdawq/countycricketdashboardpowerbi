import streamlit as st

def home_page():
    """Displays the public landing page content with improved layout."""

    # --- Centered Title and Subtitle ---
    st.markdown("<h1 style='text-align: center;'>🏏 Welcome to the County Cricketer Lovers Membership Site!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your all-in-one resource for cricket history, insights, and stats—perfect for every County Cricket enthusiast!</p>", unsafe_allow_html=True)
    st.divider() # Adds a horizontal line

    # --- Login/Signup Instructions ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔑 Already a Member?")
        st.info("Use the login details from the latest BuyMeACoffee post. Enter them in the **sidebar** to access the dashboard.")
    with col2:
        st.subheader("🚀 New Here?")
        st.success(
            "Join the County Cricketer Lover tier to get instant access! \n\n"
            "[👉 Sign up via BuyMeACoffee](https://buymeacoffee.com/leadingedgepod)"
        )

    st.divider() # Adds another horizontal line

    # --- Dashboard Preview Image ---
    st.subheader("✨ Sneak Peek Inside:")
    st.image("assets/dash.png", caption="A glimpse of the powerful member dashboard", use_container_width=True)
    st.divider() # Add another divider after the preview

    # --- Features Section ---
    st.header("📚 What You Get:")
    st.markdown("---") # Add a little space

    # Feature 1: Stats Pack
    st.subheader("📊 Join the Cricket Captain 2024 Stats Pack")
    st.markdown("Get ahead of the game with comprehensive stats.")

    # Feature 2: Ultimate Database
    st.subheader("🏏 County Championship Ultimate Database")
    st.markdown("Your central hub for all County Championship data.")

    # Feature 3: Extensive Player Stats + Image
    st.subheader("📈 Extensive Player Statistics (1890-2024)")
    st.markdown("Deep dive into historical performance across eras.")
    st.image("assets/historybatting.png", caption="Historical Batting Statistics (1890-2024)", use_container_width=True)

    # Feature 4: Ball-by-Ball
    st.subheader("🎯 Detailed Ball-by-Ball Records (2020-2024)")
    st.markdown("Analyze every single delivery from recent seasons.")

    # Feature 5: Stats vs Bowling Types + Image
    st.subheader("🆚 Player Stats vs. Bowling Types")
    st.markdown("Understand player strengths and weaknesses against different bowling styles.")
    st.image("assets/matchupbattingdata.png", caption="Batting Stats vs. Bowling Types", use_container_width=True)

    # Feature 6: Batter vs Bowler + Image
    st.subheader("⚔️ Batter vs. Bowling Matchups")
    st.markdown("Explore detailed head-to-head analysis between batters and bowlers.")
    st.image("assets/matchupdata.png", caption="Detailed Batter vs. Bowler Matchups", use_container_width=True)

    # Feature 7: Rankings + Image
    st.subheader("🏆 Player Rankings")
    st.markdown("Based on the sophisticated Cricket Draft Algorithm.")
    st.image("assets/cricketdraft.png", caption="Player Rankings using the Cricket Draft Algorithm", use_container_width=True)


    st.divider()

    st.success(
        "📖 **Ready to dive in?** Join the County Cricketer Lovers Club today via the **[BuyMeACoffee link](https://buymeacoffee.com/leadingedgepod)** above!"
    )


# Example of running this page directly (optional, for testing)
# if __name__ == "__main__":
#     st.set_page_config(layout="wide") # Add layout config for direct testing
#     home_page()