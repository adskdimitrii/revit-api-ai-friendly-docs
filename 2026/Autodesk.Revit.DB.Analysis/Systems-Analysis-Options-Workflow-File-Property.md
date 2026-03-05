# Systems Analysis Options Workflow File Property

Source: https://www.revitapidocs.com/2026/f4634304-0c9c-421f-fea4-efa6e1d527a3.htm

---

| Systems Analysis Options Workflow File Property |
| --- |

The file name of the EnergyPlus workflow script. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public string WorkflowFile { get; set; }
```

```
Public Property WorkflowFile As String
	Get
	Set
```

```
public:
property String^ WorkflowFile {
	String^ get ();
	void set (String^ value);
}
```

```
member WorkflowFile : string with get, set
```

#### Property Value

String ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The analysis requires a valid workflow file path or the empty string. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks When requesting a new system analysis, it is okay to have an empty workflowFile in the SystemsAnalysisOption. In that case,
 the ViewSystemsAnalysisReport would supply the weather file with the default value "HVAC Systems Loads and Sizing.osw". ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SystemsAnalysisOptions Class](8d8fe6a8-d3f6-c4fd-99ac-3181ba0253d6.htm) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
