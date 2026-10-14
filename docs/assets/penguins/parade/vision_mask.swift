// Usage: vmask OUTDIR in1.png in2.png ...  -> OUTDIR/<stem>_all.png plus OUTDIR/<stem>_i<k>.png per instance (8-bit soft masks at full res)
import Foundation
import Vision
import CoreImage

let args = CommandLine.arguments
let outDir = URL(fileURLWithPath: args[1])
let ctx = CIContext()
let gray = CGColorSpace(name: CGColorSpace.linearGray)!

func write(_ buf: CVPixelBuffer, _ url: URL) throws {
    let img = CIImage(cvPixelBuffer: buf)
    try ctx.writePNGRepresentation(of: img, to: url, format: .L8, colorSpace: gray)
}

for path in args.dropFirst(2) {
    let url = URL(fileURLWithPath: path)
    let stem = url.deletingPathExtension().lastPathComponent
    let handler = VNImageRequestHandler(url: url)
    let req = VNGenerateForegroundInstanceMaskRequest()
    do {
        try handler.perform([req])
        guard let obs = req.results?.first else { print("\(stem): no subject"); continue }
        let all = try obs.generateScaledMaskForImage(forInstances: obs.allInstances, from: handler)
        try write(all, outDir.appendingPathComponent("\(stem)_all.png"))
        for i in obs.allInstances {
            let m = try obs.generateScaledMaskForImage(forInstances: IndexSet(integer: i), from: handler)
            try write(m, outDir.appendingPathComponent("\(stem)_i\(i).png"))
        }
        print("\(stem): \(obs.allInstances.count) instances")
    } catch { print("\(stem): error \(error)") }
}
