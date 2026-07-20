import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS


def main():
    st.set_page_config(page_title="AI GYM Coach", page_icon="🏋️‍♂️", layout="centered", initial_sidebar_state="expanded")

    if not render_login_wall():
        return
    
    initial_session_defaults()

    workout_started = st.session_state.get("workout_started", False)

    with st.sidebar:
        st.title("🏋️‍♂️ AI Real-time GYM Trainer")

        if st.session_state.username:
            st.markdown(f"### Welcome, {st.session_state.username}!")

        st.divider()

        st.subheader("Workout Plan")

        if not workout_started:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")

            if "plan_sets" not in st.session_state:
                st.session_state["plan_sets"] = 3

            st.number_input("Sets", min_value=1, max_value=10, value=3, step=1, key="plan_sets")
            st.number_input("Reps", min_value=1, max_value=50, value=10, step=1, key="plan_reps")
            start_workout_button = st.button("Start Workout", width="stretch", key="start_workout_button")

            if start_workout_button:
                st.session_state["workout_started"] = True
                st.rerun()
        else:
            st.write("Workout in Started")
            exercise = st.session_state.get("plan_exercise", "N/A")
            sets = st.session_state.get("plan_sets", 0)
            reps = st.session_state.get("plan_reps", 0) 

            st.info(f"**{exercise}** - {sets} sets of {reps} reps")

            end_session_button = st.button("End Workout", width="stretch", key="end_workout_button")

            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()


        if workout_started:
            st.divider()
            st.subheader("Progress")

            exercise = st.session_state.get("plan_exercise")
            total_reps = st.session_state.get("reps")
            current_set_reps = st.session_state.get("current_set_reps")
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets = st.session_state.get("plan_sets")
            
            
            st.metric("Total Reps", f"{total_reps}")
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metrics")
                st.metric("Knee Angle", f"{st.session_state.knee_angle}°")
                st.metric("Back Angle", f"{st.session_state.back_angle}°")
                st.metric("Depth Status", st.session_state.depth_status)

            elif exercise == "Push-ups":
                st.subheader("Push-up Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Body Alignment", st.session_state.body_alignment)
                st.metric("Hip Position", st.session_state.hip_status)

            elif exercise == "Biceps Curls (Dumbbell)":
                st.subheader("Curl Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Shoulder Stability", st.session_state.shoulder_status)
                st.metric("Swing Detection", st.session_state.swing_status)

            elif exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Arm Extension", st.session_state.extension_status)
                st.metric("Back Arch", st.session_state.back_arch_status)

            elif exercise == "Lunges":
                st.subheader("Lunge Metrics")
                st.metric("Front Knee Angle", f"{st.session_state.front_knee_angle}°")
                st.metric("Torso Angle", f"{st.session_state.torso_angle}°")
                st.metric("Balance Status", st.session_state.balance_status)



        

    

if __name__ == "__main__":
    main()
