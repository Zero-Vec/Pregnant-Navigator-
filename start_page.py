import streamlit as st

st.markdown(
    """
<style>
    /* 主标题动画 */
    @keyframes titleAnimation {
        0% { transform: translateY(-20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    /* 主标题 */
    .main-title {
        color: #E57373;
        font-size: 2.5em;
        text-align: center;
        padding: 20px;
        border-bottom: 3px solid #E57373;
        animation: titleAnimation 0.5s ease-out;
    }
    
    /* 输入框美化 */
    .stTextInput>div>div>input {
        border-radius: 15px;
        padding: 1.2rem;
        box-shadow: 0 2px 6px rgba(255,107,107,0.2);
    }
    
    /* 动态结果卡片 */
    .result-card {
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    /* 诈骗结果样式 */
    .fraud-result {
        background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
        color: white;
    }
    
    /* 正常结果样式 */
    .normal-result {
        background: linear-gradient(135deg, #63cdda, #77ecb9);
        color: white;
    }
</style>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.expander("🌟 页面功能导航", expanded=True).write(
        """
        - 🏠 **首页**：项目简介、平台架构、项目亮点、功能概览等。
        - 🕵️ **孕心查**：心理健康筛查与报告生成。
        - 🤖 **孕心悦**：情绪管理与心理调节方案。
        - 📚 **孕知宝**：健康知识支持与教育。
        """
    )

st.markdown('<h1 class="main-title">💞欢迎来到孕心导航——智慧孕育的AIGC守护者</h1>', unsafe_allow_html=True)
# st.header("💞欢迎来到孕心导航——智慧孕育的AIGC守护者", divider="rainbow")
st.write("### 🌈项目简介")
st.write(
    "孕心导航是一个融合了心理学与人工智能技术的智能化系统，旨在为孕产妇及其家属提供全方位的健康支持。通过实现孕产期的心理筛查、情绪管理和知识普及，“孕心导航”为用户提供一站式健康服务，体现了**医工结合、智能医疗**的孕产妇护理科特征。"
)
st.write("### 平台架构")
st.write("#### 🕵️孕心查")
st.write(
"- **目标用户**：心理健康工作者")
st.write("- **功能**：通过大型语言模型（LLM）智能访谈实现孕产期抑郁和焦虑等精神疾病的初步筛查，并生成个性化的心理健康报告。")
st.write("- **特点**：提供了便捷高效的心理评估手段，减少了面对面咨询的限制，体现了智能筛查与远程诊疗的理念。")

st.write("#### 🤖孕心悦")
st.write("- **目标用户**：孕产妇个人")
st.write(
    "- **功能**：基于认知行为疗法（CBT）和强化学习技术，智能体能够识别并干预用户的情绪，提供实时、个性化的心理调节方案，帮助缓解孕产期的情绪困扰。"
)
st.write("- **特点**：体现了新医科中智能心理干预与精准医疗的特性。")

st.write("#### 👩‍💼孕知宝")
st.write("- **目标用户**：孕产妇及其家庭")
st.write(
    "- **功能**：基于检索增强生成（RAG）技术，为用户提供科学准确的健康知识支持，内容涵盖营养、运动、产后护理等方面。"
)
st.write("- **特点**：体现了新医科中“健康教育与全周期健康管理”的理念。")


st.write(
    "让我们携手并肩，在这段奇妙而充满期待的生命旅程中，一起迎接新生命的璀璨降临！"
)
st.write(
    "#### ⭐️项目亮点"
)

st.write(
    "-  **多学科交叉融合**：本项目深度整合了**自然语言处理**（NLP）与**认知行为疗法**（CBT）的核心原理，旨在**为孕产妇群体提供精准的心理健康指导**。通过模拟CBT的完整流程——从问题探讨与认知重构到行为干预，模型在对话中帮助用户调整认知模式与行为方式。项目基于MindSpore AI框架的Baichuan2_7B模型，并在曻腾AI平台上利用Ascend 910A处理器进行单机双卡的LoRA微调，自主开发出**HappyMum-GPT对话模型**。模型不仅能够在对话中深入挖掘并记录用户的**潜在心理状态，提供高度定制化的心理支持。压力来源**与**情绪问题**，还依据**依恋理论**和**角色适应理论**等心理学理论提供个性化的行为干预。结合情感分析与共情能力，该系统能够精准捕捉用户"
)
st.write(
    "-  **特殊人群定制化支持**：本项目专为孕产妇群体打造，融合了**千余条专业CBT对话语料**、**十万条单轮与双轮中文心理健康支持问答数据集**、中文心理学专业书籍内容以及**十万条临床记录**，构建出涵盖**孕前、孕期及产后**常见问题的知识库。项目采用**MindFormers**套件，并基于**讯飞星火大模型**（iflytekspark-13B）进行微调，同时结合**RAG增强生成检索技术**。模型在生成专业回答的同时，能够快速从知识库中检索相关信息，确保回答的精准性与专业性，满足不同阶段孕产妇的多样化需求。"
)
# st.write("## 🌈项目成果")
st.write(
    "-  **育儿知识服务优化**：在育儿场景中，本项目基于**MindFormers**对**InternLM书生·浦语大模型**进行了针对性微调，专注于不同育儿情境中的问题解决方案。通过优化模型的学习、数学和推理能力，确保其在育儿相关问题上的专业性与高效性。**MindFormers**套件的使用简化了模型训练与部署流程，大幅提升开发效率，推动了AI技术在育儿领域的创新应用，为父母和家庭提供了智能化的育儿支持。"
)
st.write(
    "本项目融合多学科理论与前沿AI技术，采用大规模语料与高效模型微调方法，力求在心理健康和育儿领域提供卓越的人工智能解决方案。"
)
st.write(
    "#### 📌项目实用性"
)
st.write(
    "-  **紧跟新质生产力方针**：项目采用较新的大语言模型进行训练，并**通过创新的生产要素配置**激发知识、技术与人才的潜能，充分体现新质生产力的核心价值。系统以智能化技术为驱动，提升资源整合与知识传播的效率，推动人工智能在孕期支持领域的创新发展，为孕产妇提供更精准的关怀。"
)
st.write(
    "-  **精准服务孕产期健康**：本系统通过**专业且精准的孕产期知识支持**，帮助女性在孕育过程中科学地维护自身和胎儿的健康，降低心理问题的发生风险。项目涵盖孕前准备、孕期调适、产后恢复等阶段，并在提升用户生活质量方面发挥积极作用，帮助女性从容应对生理和心理的变化。"
)
st.write(
    "-  **智能疏导孕期心理问题**：通过**HappyMum-GPT对话模型**，系统能够在对话过程中**深入挖掘并记录用户的压力源与情绪问题**。结合**依恋理论与角色适应理论**，模型为用户提供**个性化的心理疏导与行为干预**。该功能不仅能有效缓解孕期女性的情绪困扰，还帮助她们建立情绪韧性，提升整体心理健康水平，为母职角色的转变打下坚实基础。"
)
st.write(
    "#### 📑功能概览"
)
st.write(
    "-  **HappyMum-GPT咨询师**：基于MindSpore AI自主研发的**HappyMum-GPT对话模型**，该功能模拟“宝宝”与孕期女性的对话场景，帮助用户探索并识别孕期潜在的压力源和情绪问题。通过分析用户的情绪状态，结合**26类情景化情绪应对方案**，提供个性化的认知重构与行为干预建议，支持用户在孕期和产后保持心理平衡。"
)
st.write(
    "-  **孕产智能百科助手**：融合**RAG（检索增强生成）技术**与经过MindFormers微调的**讯飞星火大模型**(iflytekspark-13B)，本功能提供精确、全面的孕产期知识服务。无论是专业的医疗建议还是心理辅导，百科助手为孕产期女性及其家庭提供权威且易于理解的解答，确保身心健康和家庭福祉的全面保障。"
)
st.write(
    "-  **智能宝宝聊天机器人**：通过MindFormers套件对**书生·浦语大模型**(InternLM-7B)的微调，训练出以儿童般亲切语气进行交互的**智能宝宝机器人**，营造温馨的母子互动体验。结合依恋理论和角色适应理论，该功能不仅帮助准妈妈们提前适应母亲角色，还让她们感受与宝宝沟通的乐趣和情感连接，为未来的母职生活奠定情感基础。"
)
st.write(
    "#### 🌞为什么选择孕心导航？"
)
st.write(
    "-  **全面的孕期知识**：孕心导航结合**优质咨询数据集、真实临床记录**和**丰富的育儿知识问答**，为孕期女性提供**全方位的知识支持**。从孕前准备到产后护理，系统涵盖每一个关键阶段，确保用户获得专业、科学且易于理解的指导。"
)
st.write(
    "-  **智能问答服务**：基于**MindSpore平台**开发的智能心理咨询模型，孕心导航帮助用户**快速解决孕期中的各种疑问**，并有效缓解心理焦虑。通过**实时智能对话**，用户可以随时随地获取温暖的陪伴与支持，为孕期生活增添信心与安心感。"
)
st.write(
    "-  **专业心理疗法支持**：系统依托**依恋理论**与**角色适应理论**，并结合**CBT认知行为疗法**，为孕产妇提供**专业的心理疏导**。通过**持续情绪监测**，系统能及时识别情绪波动，并提供个性化的干预方案，帮助用户维持**健康、平衡的心理状态**，从而更好地迎接孕期和母职生活的挑战。"
)
st.write(
    "-  **适应多场景的个性化支持**：孕心导航不仅关注用户的身体健康，还能根据不同孕期阶段的需求提供**定制化的心理与育儿支持**。系统涵盖**孕前、孕期、产后**的常见问题，为女性在各种生活场景中提供便捷高效的帮助，让孕期生活更加从容。"
)
st.write(
    "-  **实践经验验证**：孕心导航已与多家**月子中心**达成合作，通过实践应用积累了丰富的经验。这些合作成果充分验证了系统的**有效性与实用性**。用户可以放心选择孕心导航，获得专业、可靠的孕期支持，让每一天都充满关怀与温暖，轻松迎接新生命的到来。"
)
st.write(
    "#### 👼开启孕心导航的全新旅程"
)
st.write(
    "**孕心导航**是孕产期旅程中的**智能科学助手**，专为孕产妇群体提供全面而贴心的支持。孕心导航不仅随时能够解答孕期和产后阶段的各种疑问，还能够**实时监测情绪变化**，帮助缓解焦虑情绪，保障心理健康。通过智能化支持，孕心导航帮助孕产妇**从容应对生理和心理的变化**，提供**便捷、高效、科学**的管理体验。立即开启孕心导航，让每一天都充满信心与温暖，轻松迎接新生命的到来。"
)
st.write(
    "-----------------------------------------------------------------------------------------------------------------------------------"
)
st.write(
    "#### 💞**孕心导航**——智慧孕育的AIGC守护者，伴随孕产妇轻松走过这段特殊而美好的生命旅程。"
)
