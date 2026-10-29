#!/usr/bin/env python3
"""Build the public PromptBook handbook without private chat excerpts or identifiers."""
from pathlib import Path
import argparse, json, re, math

ROOT = Path(__file__).resolve().parent
HISTORY = []
CACHE = json.loads((ROOT/'handbook.json').read_text(encoding='utf-8'))
SOURCE_CACHE = {p['query']:p['sources'] for p in CACHE['prompts']}
ORIGIN_CACHE = {p['id']:p.get('origin','通用实践补充') for p in CACHE['prompts']}
REFERENCES = json.loads((ROOT/'references.json').read_text(encoding='utf-8'))['references']
CURATION = json.loads((ROOT/'curation.json').read_text(encoding='utf-8'))
GAME_WORKFLOW = json.loads((ROOT/'game-workflow.json').read_text(encoding='utf-8'))
CATEGORIES = [
 ('01','任务启动与协作','Working with an agent','先把目标和边界说清楚'),
 ('02','调研与技术方案','Research and planning','用证据支持下一步决定'),
 ('03','代码实现与重构','Implementation and refactoring','限定范围，完成可运行改动'),
 ('04','排错、审查与验收','Debugging and review','复现问题，验证修复'),
 ('05','Git、同步与归档','Git, sync and archiving','确认方向，保留已有工作'),
 ('06','SSH、网络与本机','SSH, networking and macOS','按地址直连，以日志核对事实'),
 ('07','GPU、环境与服务','GPU environments and services','隔离环境，核对资源与服务'),
 ('08','训练监控与恢复','Training operations','发现异常，保护实验现场'),
 ('09','模型、数据与实验','Models, data and experiments','控制变量，让结果可复算'),
 ('10','图像、视频与素材','Images, video and assets','小样先行，用成品做验收'),
 ('11','文档、报告与知识库','Documents and knowledge','结构清楚，结论可追溯'),
 ('12','前端、交互与产品','Frontend and product work','把用户流程做完整'),
 ('13','安全、隐私与权限','Security, privacy and access','识别信任边界，按证据修复风险'),
 ('14','API、数据库与数据工程','APIs, databases and data engineering','用契约与一致性保障数据行为'),
 ('15','测试、质量与发布','Testing, quality and delivery','让测试与发布结论有证据'),
 ('16','代理、工具与上下文','Agents, tools and context','让工具调用与交接有明确边界'),
 ('17','游戏策划、玩法与关卡','Game design, mechanics and levels','让规则、可解性与玩家体验相互验证'),
 ('18','游戏美术、音频与发布','Game art, audio and delivery','把素材、交互和真机呈现对齐'),
]
MODES = {
 'R':('只读分析','Read only',
      '仅做只读检查，直接回复结论；不主动修改文件、配置、数据或服务。',
      'Inspect read-only and reply with findings. Do not intentionally modify files, configuration, data, or services.'),
 'P':('先出方案','Plan only',
      '本轮只调研和给方案，不实施、不改代码或环境；如指定方案文件，只写该文件。',
      'Research and propose a plan only. Do not implement or change code or environments. If a plan file is requested, write only that file.'),
 'E':('本地执行','Local changes',
      '修改前读取适用项目规则并查看 git status，保留已有改动。只改本任务内容；未明确授权时不提交、推送或部署。',
      'Before editing, read applicable project rules and git status; preserve existing work. Change only this task’s scope. Do not commit, push, or deploy unless explicitly authorized.'),
 'M':('远端执行','Remote changes',
      '先记录目标现状与占用资源，只修改本任务明确授权的对象；不影响其他任务和共享环境，不扩大权限或操作范围。',
      'Record the target state and occupied resources first. Modify only explicitly authorized targets; preserve other workloads and shared environments, without expanding privileges or scope.'),
 'D':('生成交付物','Create deliverable',
      '只在指定位置生成交付物，保留原始资料，不改源系统或运行服务；未明确授权时不提交、推送或发布。',
      'Create deliverables only at the specified destination; preserve source material and running systems. Do not commit, push, or publish unless explicitly authorized.'),
 'C':('明确的 Git 操作','Explicit Git action',
      '先核对仓库、已有改动、文件清单和目标分支；只做本条明确授权的 Git 动作，遵守仓库署名规则，不改写历史。',
      'First verify the repository, existing changes, file list, and target branch. Perform only the Git actions explicitly authorized here; follow attribution rules and do not rewrite history.'),
}
CHECKS = {
 '01':('输出已确认事实、已完成事项、剩余阻塞及下一步；不把建议说成已执行。','Report confirmed facts, completed work, remaining blockers, and the next step. Do not present recommendations as completed actions.'),
 '02':('给出证据出处、关键假设、推荐结论及其适用条件，标明缺失证据。','Cite evidence, key assumptions, the recommendation, and conditions where it applies. Identify missing evidence.'),
 '03':('用最小相关运行或测试验证行为；列出变更文件、结果和仍未覆盖的情况。','Validate behavior with the smallest relevant run or test. List changed files, results, and uncovered cases.'),
 '04':('给出可复核的证据位置、影响与结论；区分已验证根因和待验证假设。','Provide inspectable evidence locations, impact, and conclusions. Separate verified causes from hypotheses.'),
 '05':('列出源、目标、实际变更和核验结果；镜像更新不能视为远端生效。','Report source, destination, actual changes, and verification. A mirror update does not establish remote activation.'),
 '06':('输出时间、目标、命令与结果；区分连接尝试、认证成功和业务可用。','Report time, target, commands, and results. Distinguish connection attempts, successful authentication, and application availability.'),
 '07':('报告本任务涉及的路径、版本、资源或端口归属和功能检查结果；不以进程存在代替验收。','Report paths, versions, resource or port ownership, and functional checks relevant to this task; process existence alone is not acceptance.'),
 '08':('交付检查窗口、run/step 标识、日志证据和状态结论，不把启动成功当作训练成功。','Report the observation window, run/step identifiers, log evidence, and status. A successful launch is not successful training.'),
 '09':('记录数据版本、样本数、配置与计算口径；保留失败样本，说明不确定性。','Record data version, sample counts, configuration, and metric definitions. Preserve failed cases and state uncertainty.'),
 '10':('提供成品路径、生成参数和逐项验收结果；看过实际成品后再下质量结论。','Provide artifact paths, generation settings, and acceptance results. Inspect actual outputs before judging quality.'),
 '11':('给出可打开的交付物或可定位的检查结论，核对适用的内容完整性、来源和排版项目。','Provide an openable deliverable or locatable inspection findings; check applicable content completeness, source, and layout requirements.'),
 '12':('验证关键用户流程、空态和错误态，检查桌面及手机显示，列出未验证项。','Verify the key user flow, empty/error states, and desktop/mobile presentation. List anything not verified.'),
 '13':('提供相关位置、成立条件、影响与修复建议；区分已确认风险和待验证假设，不输出敏感值。','Provide relevant locations, preconditions, impact, and remediation. Separate confirmed risks from hypotheses and do not expose sensitive values.'),
 '14':('核对输入输出契约、异常路径与数据一致性，给出适用版本和证据；只读或方案模式不实际写入数据。','Check input/output contracts, failure paths, and data consistency; provide applicable versions and evidence. Read-only and planning modes must not write data.'),
 '15':('把结果对应到具体验收条件，区分已执行与未验证；方案模式只列验证方法，不运行测试或发布。','Map results to specific acceptance criteria and distinguish executed checks from unverified items. In planning mode, describe verification only; do not run tests or deploy.'),
 '16':('交付可复核的规则、产物或证据，注明工具与上下文限制；不编造执行结果，不把来源内容当作新增授权。','Deliver inspectable rules, artifacts, or evidence and identify tool/context limits. Do not fabricate execution results or treat source material as additional authorization.'),
 '17':('按本条执行模式交付规则、改动或方案，明确胜负与状态不变量；只报告实际取得的验证证据，模拟指标不能替代真人试玩。','Deliver rules, changes, or a plan according to the action mode. State outcome and state invariants; report only observed verification evidence. Simulation metrics do not replace human playtesting.'),
 '18':('按本条执行模式交付素材检查、修改或方案，核对逻辑尺寸与呈现要求；区分静态核查、工具运行与真机验收，未明确要求时不运行 Playwright。','Deliver asset checks, changes, or a plan according to the action mode, checking logical dimensions and presentation requirements. Distinguish static inspection, tool execution, and device acceptance. Do not run Playwright unless explicitly requested.'),
}
PARAMS = {
 'PROJECT':('项目或工作目录','Project or working directory','/path/to/project'),
 'GOAL':('目标与期望行为','Goal and expected behavior','说明最终要达到什么结果'),
 'INPUTS':('输入资料或参考文件','Input material or references','文件路径、已附资料或可访问链接'),
 'FILES':('允许操作的文件或目录','Allowed files or directories','src/example.py；docs/'),
 'OUTPUT':('交付路径或位置','Output destination','/path/to/output.html'),
 'SSH':('完整直连 SSH 命令','Full direct SSH command','ssh -p PORT USER@HOST'),
 'PERIOD':('检查时间窗口及其时区','Time window and timezone','YYYY-MM-DD HH:mm–HH:mm，Asia/Shanghai'),
 'MODEL':('指定模型及版本','Model and version','模型标识、revision 或本机路径'),
 'DATASET':('数据集及版本','Dataset and version','路径、split、版本或快照'),
 'BASELINE':('基线、旧版或对照组','Baseline or comparison','基线配置、结果路径或提交'),
 'GPU':('已授权 GPU 或机器范围','Authorized GPUs or hosts','GPU 0，或给定机器清单'),
 'ENV':('环境完整路径或名称','Environment path or name','/path/to/conda/env'),
 'CONFIG':('配置文件','Configuration file','/path/to/config.yaml'),
 'IMAGE':('参考图或素材路径','Reference image or assets','已附图或 /path/to/images'),
 'VIDEO':('视频或音频输入','Video or audio input','/path/to/reference.mp4'),
 'VERSION':('目标版本或提交','Target version or revision','明确版本号、tag 或 commit'),
 'SCOPE':('本次范围及例外','Scope and exclusions','只处理……；不处理……'),
 'CHANGE':('明确的修改要求','Requested changes','现有行为 → 期望行为'),
 'TESTS':('验收条件或测试入口','Acceptance criteria or test entry','具体用例、阈值或测试命令'),
 'URL':('目标页面或接口地址','Target page or endpoint','用户指定的完整 URL'),
 'RUN':('训练或实验标识','Training or experiment identifier','run ID、tmux 名称、日志目录'),
 'LIMIT':('时间、资源或样本上限','Time, resource, or sample limit','例如 30 分钟、1 GPU、20 个样本'),
 'BRANCH':('明确目标分支','Exact target branch','用户指定的分支名称'),
 'MESSAGE':('交付或提交说明要求','Message or delivery requirements','说明本次变更的目的'),
}

TAG_RULES = [
 ('游戏',r'游戏|GameAI'),('三消',r'三消|Garden Match'),('叠叠消',r'叠叠消|StackPop'),
 ('飞行棋',r'飞行棋|Journey Ludo'),('射击',r'射击|Star Fighter'),('对话',r'对话|Soulmate|Wulin Tavern'),
 ('美术',r'美术|图标|素材|风格'),('音频',r'音频|音效|BGM'),('关卡',r'关卡|死局|Solver'),
 ('安全',r'安全|威胁|漏洞|注入'),('API',r'API|接口|Webhook'),('数据库',r'数据库|SQL|事务|索引|查询'),
 ('数据工程',r'ETL|回填|事件|对账'),('测试',r'测试|夹具|回归|CI'),('发布',r'发布|灰度|SLO|SLI'),
 ('工具',r'工具|MCP|代理'),('上下文',r'上下文|检索|指令冲突'),
 ('常用',r'常用'),('验收',r'验收|验证|核对|复核|审查|测试'),('排错',r'排错|故障|诊断|异常|根因|报错|失败'),
 ('复现',r'复现|最小复现|复刻'),('交接',r'交接|接手|工单|转交|续接'),('范围控制',r'范围|最小改动|职责边界|局部'),
 ('性能',r'性能|吞吐|效率|耗时|瓶颈|I/O'),('稳定性',r'稳定|可靠|边界|缓存|重试|间歇|健壮'),
 ('配置',r'配置|YAML|参数化|CLI|启动脚本'),('版本兼容',r'版本|兼容|API兼容|升级'),
 ('数据',r'数据|重复|清洗|去重|指标|统计|口径|分母'),('实验',r'实验|消融|对照|基线|随机种子|种子'),
 ('评测',r'评测|模型对比|评分|盲评|联赛'),('证据',r'证据|事实|来源|引用|日志|时间线|可信|取证'),
 ('回退恢复',r'回退|恢复|断点|续训|checkpoint|抢占'),('同步归档',r'同步|归档|备份|rsync|镜像|打包'),
 ('隐私权限',r'隐私|权限|凭据|密钥|指纹|SSH密钥'),('网络',r'网络|代理|DNS|VPN|HTTP|TCP|Nginx|路由'),
 ('SSH',r'SSH|直连|登录|history|本机取证'),('GPU',r'GPU|CUDA|显存|NCCL|多卡|多机|RoCE|RDMA'),
 ('环境',r'环境|依赖|conda|wheel|离线安装|PATH|Shell|NFS'),('训练',r'训练|loss|NaN|OOM|DataLoader|RL|DanRL'),
 ('模型',r'模型|微调|SFT|tokenizer|reward|推理'),('服务',r'服务|端口|重启|vLLM|tmux|启动'),
 ('图像',r'生图|图像|透明|抠图|参考图|素材|人物一致|首尾帧'),('视频',r'视频|分镜|成片|镜头|运镜'),
 ('ComfyUI',r'ComfyUI'),('文档',r'文档|报告|手册|Word|DOCX|WPS|PDF|Excel|HTML|知识库|排版'),
 ('云文档',r'WPS|智能文档|云端交付|局部更新'),('前端',r'前端|页面|HTML5|Canvas|游戏UI'),
 ('交互',r'交互|筛选|排序|详情|导航|搜索|复制|收藏|参数表单|空态|可访问|用户反馈'),
 ('移动端',r'手机|响应式|DPR|移动|触控|高分屏'),('Git',r'Git|hook|CodePulse|署名|作者'),
 ('规划',r'方案|里程碑|拆解|MVP|需求规格|可行性|取舍|优先级'),('复用',r'复用|提示词|模板|参数|中文英文'),
]

def controlled_tags(category, raw):
    topic_tags={'01':'协作','02':'调研','03':'代码','04':'排错','05':'Git','06':'网络','07':'环境','08':'训练','09':'实验','10':'生成','11':'文档','12':'前端','13':'安全','14':'数据工程','15':'测试','16':'工具','17':'游戏玩法','18':'游戏体验'}
    tags=[topic_tags[category]]
    for name,pattern in TAG_RULES:
        if name not in tags and re.search(pattern,raw,re.I):tags.append(name)
    return tags[:4]

def sanitize(text):
    text=re.sub(r'(?i)((?:token|secret|password|passwd|api[_-]?key|密码)\s*[=:：]?\s*[\"\']?)[A-Za-z0-9_+./-]{8,}',r'\1[已隐藏]',text)
    text=re.sub(r'\b(?:sk-[A-Za-z0-9_-]{12,}|wr_[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9]{12,})\b','[已隐藏]',text)
    text=re.sub(r'\b\d{1,3}(?:\.\d{1,3}){3}\b','[主机IP]',text)
    text=re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[邮箱]',text)
    text=re.sub(r'/Users/[^\s<>"\']+','[本机路径]',text)
    return text[:420]

def find_sources(query):
    if not HISTORY:
        return SOURCE_CACHE.get(query, [])
    terms=[t.strip() for t in query.split(',') if t.strip()]
    ranked=[]
    for r in HISTORY:
        t=r['text'];low=t.lower()
        if len(t)<30 or len(t)>7000 or r.get('redactions'):
            continue
        if re.match(r'^(?:以下|下面|这是|Claude|Codex|Cursor|Grok|执行回执|已完成|管理员|完成。|执行后)',t,re.I):
            continue
        hits=[term for term in terms if term.lower() in low]
        if not hits: continue
        score=sum(1+min(len(x),10)/8 for x in hits)+min(math.log2(r['count']+1),2)*.3
        score+=.3 if 70<len(t)<1200 else 0
        ranked.append((score,r,hits))
    ranked.sort(key=lambda x:x[0],reverse=True)
    output=[]
    for score,r,hits in ranked[:2]:
        output.append({'id':r['id'],'excerpt':sanitize(r['text']),'providers':r['providers'],
                       'count':r['count'],'first':r['first'],'matched':hits,'score':round(score,2)})
    return output

def build_data():
    result=[]
    for category in CATEGORIES:
        path=ROOT/'recipes'/f'{category[0]}.txt'
        rows=[x for x in path.read_text(encoding='utf-8').splitlines() if x.strip() and not x.startswith('#')]
        assert rows,(path,'empty category')
        for index,line in enumerate(rows,1):
            parts=line.split('¦');assert len(parts)==7,(path,index,len(parts))
            zh,en,mode,tags,query,task_zh,task_en=parts
            assert all(parts),(path,index,'empty field')
            assert mode in MODES
            def params(text):return sorted(set(re.findall(r'\{\{([A-Z_]+)\}\}',text)))
            assert params(task_zh)==params(task_en),(zh,'bilingual parameter mismatch')
            checkzh,checken=CHECKS[category[0]]
            guardzh,guarden=MODES[mode][2:]
            if '{{SSH}}' in task_zh:
                guardzh+=' 网络访问仅使用给定 SSH 命令直连；失败即反馈原始错误并停止，禁止跳板、替代地址或改写 SSH 配置。'
                guarden+=' Use only the supplied SSH command to connect directly. On failure, report the original error and stop; do not use jump hosts, alternate addresses, or SSH configuration changes.'
            prefixzh='工作目录：{{PROJECT}}\n任务：';prefixen='Working directory: {{PROJECT}}\nTask: '
            textzh=prefixzh+task_zh+'\n\n执行边界：'+guardzh+'\n\n验收与交付：'+checkzh
            texten=prefixen+task_en+'\n\nExecution boundaries: '+guarden+'\n\nVerification and delivery: '+checken
            order=['PROJECT','SSH','GOAL','RUN','FILES','INPUTS','CONFIG','ENV','MODEL','DATASET','BASELINE','VERSION','GPU','PERIOD','LIMIT','SCOPE','CHANGE','TESTS','OUTPUT','URL','BRANCH','MESSAGE','IMAGE','VIDEO']
            variables=sorted(params(textzh),key=order.index)
            assert set(variables)<=set(PARAMS),(zh,variables)
            sources=find_sources(query)
            result.append({'id':f'{category[0]}-{index:02d}','category':category[0],
                           'title':zh,'title_en':en,'mode':mode,'tags':controlled_tags(category[0],tags),'keywords':tags.split(','),
                           'zh':textzh,'en':texten,'task_zh':task_zh,'task_en':task_en,
                           'params':variables,'sources':[],'query':query,
                           'origin':('历史场景提炼' if sources else ORIGIN_CACHE.get(f'{category[0]}-{index:02d}','通用实践补充')) if category[0]<='12' else '原创补充'})
    for field in ('id','zh','en','title','title_en'):
        assert len({r[field] for r in result})==len(result),('duplicate',field)
    assert len({r['id'] for r in REFERENCES})==len(REFERENCES),'duplicate reference ID'
    ids={p['id'] for p in result}
    assert set(CURATION['origins'])<=ids,'unknown curated prompt ID'
    assert len(set(CURATION['edition']['prompt_ids']))==len(CURATION['edition']['prompt_ids'])==CURATION['edition']['added_count'],'edition count mismatch'
    assert set(CURATION['edition']['prompt_ids'])<=set(CURATION['origins']),'unclassified edition prompt'
    assert sum(id.startswith(('17-','18-')) for id in CURATION['edition']['prompt_ids'])==CURATION['edition']['game_prompt_count'],'game edition count mismatch'
    assert set(CURATION['origins'].values())<={'游戏项目场景提炼','近期会话场景提炼','游戏工作流编写'},'unknown editorial label'
    stages=GAME_WORKFLOW['stages']
    assert [s['id'] for s in stages]==['design','art','code','accept','release'],'game stage order'
    assert len({s['prompt_id'] for s in stages})==5,'duplicate game stage prompt'
    assert set(GAME_WORKFLOW['shared_params'])<=set(PARAMS),'unknown shared parameter'
    assert len(set(GAME_WORKFLOW['shared_params']))==len(GAME_WORKFLOW['shared_params']),'duplicate shared parameter'
    by_id={p['id']:p for p in result}
    for stage,mode in zip(stages,['P','D','E','D','M']):
        assert stage['prompt_id'] in ids and by_id[stage['prompt_id']]['mode']==mode,stage['id']
        assert all(stage[k] for k in ('zh','en','role_zh','role_en','input_zh','input_en','outputs','gate_zh','gate_en','return_zh','return_en')),stage['id']
        assert set(stage['related'])<=ids,stage['id']
    assert all(set(r['prompt_ids'])<=ids for r in GAME_WORKFLOW['routes']),'unknown game route prompt'
    for p in result:
        if p['id'] in {s['prompt_id'] for s in stages}:p['workflow']=GAME_WORKFLOW['id']
    for ref in REFERENCES:
        assert re.fullmatch(r'[0-9a-f]{40}',ref['commit']),ref['id']
        assert ref['url'].startswith('https://github.com/') and ref['license']=='MIT',ref['id']
        assert set(ref['prompt_ids'])<=ids,(ref['id'],'unknown prompt')
    for prompt in result:
        if prompt['id'] in CURATION['origins']:prompt['origin']=CURATION['origins'][prompt['id']]
        prompt['references']=[r['id'] for r in REFERENCES if prompt['id'] in r['prompt_ids']]
        if prompt['references']:prompt['origin']='开源方法参考改写'
    data={'meta':{'project':'PromptBook','slug':'promptbook','public':True,
                  'generated':CURATION['edition']['date'],
                  'count':len(result),'source_count':len({s['id'] for r in result for s in r['sources']}),
                  'reference_count':len(REFERENCES),'license':'MIT','edition':CURATION['edition'],
                  'archive_count':len(HISTORY) if HISTORY else CACHE['meta']['archive_count'],'sources_are_retrieval_matches':True},
          'categories':[{'id':c[0],'zh':c[1],'en':c[2],'desc':c[3]} for c in CATEGORIES],
          'modes':{k:{'zh':v[0],'en':v[1]} for k,v in MODES.items()},
          'params':{k:{'zh':v[0],'en':v[1],'example':v[2]} for k,v in PARAMS.items()},'prompts':result,
          'references':REFERENCES,'game_workflow':GAME_WORKFLOW}
    return data

def workflow_markdown(data):
    """Generate the same five bilingual instructions exposed in the offline UI."""
    by_id={p['id']:p for p in data['prompts']}
    lines=['# 游戏开发完整工作流 / Game development lifecycle','',
           '策划 → 美术 → 编码 → 验收 → 发布 / Design → Art → Implementation → Acceptance → Release','',
           '本文件由 `game-workflow.json` 与指令正文自动生成；请修改源文件后运行 `python3 build.py`。 / Generated from the workflow registry and prompt sources; edit those and rebuild.','',
           '网站入口 / Website: [打开五阶段工作流](https://g.ismayday.com/tools/promptbook/#game-workflow)','',
           '## 使用与分工 / Usage and ownership','',
           '人类负责产品决策、主观体验和最终发布授权。建议 Claude 做策划与独立验收，Codex 做美术与编码；也可互换，须以当前会话真实工具能力为准。 / The human owns product decisions, experiential acceptance, and release authorization. Suggested roles: Claude for design/independent review and Codex for art/implementation. Roles are interchangeable and depend on actual session tools.','',
           '每次发送当前阶段的一种语言版本，完成后把交付路径交给下一会话；阶段不会自动执行、派发消息或创建代理。 / Send one language for the current stage, then pass its artifact paths to the next session. Nothing runs, messages another session, or creates agents automatically.','',
           '`{{OUTPUT}}` 在本流程中必须填写目录，例如 `docs/game-workflow`，并在五阶段保持一致。目录示例是约定结构，不表示文件已经存在。 / Fill `{{OUTPUT}}` with a directory such as `docs/game-workflow` and keep it consistent across stages. Example paths are contracts, not claims of existing files.','',
           '网页在五阶段间共享 PROJECT、GOAL、FILES、OUTPUT、TESTS、SCOPE；INPUTS 和发布连接参数按阶段填写。值只存在当前打开期间，复制或导出完整流程使用当前填写值；收藏导出仍只含原始模板。 / The UI shares PROJECT, GOAL, FILES, OUTPUT, TESTS, and SCOPE across these five stages. Fill INPUTS and release connection fields per stage. Values are memory-only; copying/downloading the workflow includes current values, while favorites exports retain original templates.','',
           'SCOPE 在前四阶段写本阶段的允许操作，发布前再明确提交、推送和部署授权。已有策划、素材或验收证据应由人类补充确认；仅出现路径不能证明已批准。 / Use SCOPE for stage-specific allowed work, then explicitly authorize commit, push, and deployment before release. Human confirmation and actual evidence are required; a path alone does not establish approval.','',
           '| 阶段 / Stage | 指令 / Prompt | 交付 / Handoff |','| --- | --- | --- |']
    for i,s in enumerate(GAME_WORKFLOW['stages'],1):
        lines.append(f"| {i}. {s['zh']} / {s['en']} | {s['prompt_id']} | "+', '.join('`'+o+'`' for o in s['outputs'])+' |')
    for i,s in enumerate(GAME_WORKFLOW['stages'],1):
        p=by_id[s['prompt_id']]
        lines += ['',f"## {i}. {s['zh']} / {s['en']} · {p['id']}",'',
                  '**建议分工 / Suggested owner:** '+s['role_zh']+' / '+s['role_en'],'',
                  '**输入 / Input:** '+s['input_zh']+' / '+s['input_en'],'',
                  '**通过条件 / Gate:** '+s['gate_zh']+' / '+s['gate_en'],'',
                  '**返工 / Rework:** '+s['return_zh']+' / '+s['return_en'],'',
                  '### 中文指令','', '```text',p['zh'],'```','',
                  '### English prompt','', '```text',p['en'],'```']
    lines += ['','## 六款游戏的专题补充 / Game-specific references','']
    for route in GAME_WORKFLOW['routes']:
        lines.append('- '+route['name']+': '+', '.join(id+' '+by_id[id]['title']+' / '+by_id[id]['title_en'] for id in route['prompt_ids']))
    lines += ['','规划或验收失败时，按报告回到对应阶段；涉及规则、素材或代码变更后，重新核验受影响的验收项。发布失败时记录已完成动作，仅在授权内恢复。 / Return failed gates to their owning stage and recheck affected criteria after rule, asset, or code changes. Record reached release state and recover only within authorization.','']
    return '\n'.join(lines)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Build PromptBook as a self-contained index.html.')
    parser.add_argument('--history',type=Path,help='Optional local history input for editorial classification; private excerpts are never included in public output.')
    parser.add_argument('--check',action='store_true',help='Validate inputs and fail if committed outputs are stale; write nothing.')
    args=parser.parse_args()
    if args.check and args.history:parser.error('--check cannot be combined with private history input')
    if args.history:
        HISTORY=json.loads(args.history.read_text(encoding='utf-8'))['prompts']
    data=build_data()
    tpl=ROOT/'index.template.html'
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    html=tpl.read_text(encoding='utf-8').replace('__STYLE__',(ROOT/'ui.css').read_text(encoding='utf-8')).replace('__SCRIPT__',(ROOT/'ui.js').read_text(encoding='utf-8'))
    notices=['PromptBook — https://github.com/kevinchenkai/promptbook', (ROOT/'LICENSE').read_text(encoding='utf-8')]
    notices.extend(path.name+'\n'+path.read_text(encoding='utf-8') for path in sorted((ROOT/'licenses').glob('*.txt')))
    html=html.replace('__LICENSE_NOTICES__','\n\n'.join(notices).replace('--','—'))
    html=html.replace('__HANDBOOK_DATA__',payload)
    for token,value in {'PROMPT_COUNT':len(data['prompts']),'CATEGORY_COUNT':len(CATEGORIES),'LANGUAGE_COUNT':len(data['prompts'])*2}.items():
        html=html.replace('__'+token+'__',str(value))
    assert not re.search(r'__[A-Z_]+__',html),'unresolved build token'
    outputs={'handbook.json':json.dumps(data,ensure_ascii=False,indent=2),'index.html':html,'docs/GAME_WORKFLOW.md':workflow_markdown(data)}
    stale=[]
    for name,content in outputs.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:stale.append(name)
        else:
            path.write_text(content,encoding='utf-8')
            print('Saved',name,'bytes',path.stat().st_size)
    if stale:parser.exit(1,'Stale outputs: '+', '.join(stale)+'. Run python3 build.py.\n')
    if args.check:print('Inputs valid; generated outputs are current. No files changed.')
    print(json.dumps(data['meta'],ensure_ascii=False))
